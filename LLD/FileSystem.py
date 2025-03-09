class DirectoryNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}  # Stores subdirectories as {name: DirectoryNode}

    def add_child(self, name):
        if name not in self.children:
            self.children[name] = DirectoryNode(name, self)
    
    def get_child(self, name):
        return self.children.get(name)


class VirtualFileSystem:
    def __init__(self):
        self.root = DirectoryNode("/")  # Root directory
        self.current = self.root  # Start at root

    def change_directory(self, path):
        if path == "/":
            self.current = self.root
            return
        
        path_parts = path.split("/")  # Handle nested paths
        temp = self.current

        for part in path_parts:
            if part == "..":  # Move up
                if temp.parent:
                    temp = temp.parent
            elif part in temp.children:  # Move into child directory
                temp = temp.children[part]
            else:
                print(f"Error: Directory '{path}' does not exist.")
                return
        
        self.current = temp  # Update the current directory

    def get_prompt(self):
        """Returns the shell-like prompt with the current directory."""
        path = []
        node = self.current
        while node.parent:  # Traverse up to the root
            path.append(node.name)
            node = node.parent
        return "/" + "/".join(reversed(path)) + " > "

    def run(self):
        """Runs the interactive terminal loop."""
        while True:
            try:
                command = input(self.get_prompt()).strip()

                if command == "exit":
                    print("Exiting virtual terminal...")
                    break
                elif command.startswith("cd "):
                    _, path = command.split(" ", 1)
                    self.change_directory(path)
                elif command.startswith("mkdir "):  # Create directories for testing
                    _, name = command.split(" ", 1)
                    self.current.add_child(name)
                else:
                    print(f"Unknown command: {command}")

            except KeyboardInterrupt:
                print("\nExiting virtual terminal...")
                break


# Run the virtual terminal
if __name__ == "__main__":
    vfs = VirtualFileSystem()
    vfs.run()
