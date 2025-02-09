import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import requests
import time
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Flask(__name__)

# Directory to store uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload_chunk", methods=["POST"])
def upload_chunk():
    """Handles chunked file uploads."""
    file = request.files["file"]
    chunk_number = int(request.form["chunk_number"])
    total_chunks = int(request.form["total_chunks"])
    filename = secure_filename(request.form["filename"])

    # Temp directory to store chunks
    chunk_folder = os.path.join(app.config["UPLOAD_FOLDER"], f"{filename}_chunks")
    os.makedirs(chunk_folder, exist_ok=True)

    # Save each chunk
    chunk_path = os.path.join(chunk_folder, f"chunk_{chunk_number}")
    file.save(chunk_path)

    # If all chunks are received, merge them
    if chunk_number + 1 == total_chunks:
        merge_chunks(filename, chunk_folder)

    return jsonify({"message": "Chunk received", "chunk_number": chunk_number})

def merge_chunks(filename, chunk_folder):
    """Merges chunks into the final file."""
    final_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    with open(final_path, "wb") as final_file:
        for i in sorted(os.listdir(chunk_folder), key=lambda x: int(x.split("_")[1])):
            chunk_path = os.path.join(chunk_folder, i)
            with open(chunk_path, "rb") as chunk:
                final_file.write(chunk.read())

    # Cleanup temporary chunk folder
    for chunk in os.listdir(chunk_folder):
        os.remove(os.path.join(chunk_folder, chunk))
    os.rmdir(chunk_folder)

    print(f"File {filename} assembled successfully.")

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

# Flask backend URL
UPLOAD_URL = "http://127.0.0.1:5000/upload_chunk"

def upload_file_in_chunks(file_path, chunk_size=4 * 1024 * 1024):
    """Splits and uploads a file in chunks."""
    filename = os.path.basename(file_path)
    total_size = os.path.getsize(file_path)
    total_chunks = (total_size // chunk_size) + (1 if total_size % chunk_size > 0 else 0)

    with open(file_path, "rb") as file:
        for chunk_number in range(total_chunks):
            chunk = file.read(chunk_size)
            files = {"file": (filename, chunk)}
            data = {
                "chunk_number": chunk_number,
                "total_chunks": total_chunks,
                "filename": filename
            }
            response = requests.post(UPLOAD_URL, files=files, data=data)

            if response.status_code == 200:
                print(f"Uploaded chunk {chunk_number + 1}/{total_chunks}")
            else:
                print(f"Failed to upload chunk {chunk_number + 1}")

'''File Sync'''

SERVER_URL = "http://127.0.0.1:5000/sync_file"

class FileChangeHandler(FileSystemEventHandler):
    """Detects file changes and triggers sync."""

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")
        sync_file(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"File created: {event.src_path}")
        sync_file(event.src_path)

def sync_file(file_path):
    """Uploads the modified file to the server."""
    with open(file_path, "rb") as f:
        file_data = f.read()
    
    # Calculate file checksum
    file_checksum = hashlib.md5(file_data).hexdigest()

    files = {"file": open(file_path, "rb")}
    data = {"checksum": file_checksum}

    response = requests.post(SERVER_URL, files=files, data=data)
    if response.status_code == 200:
        print("File synced successfully.")
    else:
        print("Sync failed.")

UPLOAD_FOLDER = "server_sync_folder"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

file_checksums = {}

@app.route("/sync_file", methods=["POST"])
def sync_file():
    """Receives file updates and stores only modified files."""
    file = request.files["file"]
    filename = file.filename
    file_data = file.read()

    new_checksum = hashlib.md5(file_data).hexdigest()

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if filename in file_checksums and file_checksums[filename] == new_checksum:
        return jsonify({"message": "File already up-to-date"}), 200

    with open(file_path, "wb") as f:
        f.write(file_data)

    file_checksums[filename] = new_checksum

    return jsonify({"message": "File updated successfully"}), 200
