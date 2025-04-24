class File:
    def __init__(self, filename, filesize, parent):
        self.filename = filename
        self.filesize = filesize
        self.parent = parent

class Directory:
    def __init__(self, dirname,dirsize,parent = None,children = []):
        self.dirname = dirname
        self.dirsize  = dirsize
        self.parent = parent
        self.children = children
        self.files = []

class Filesystem:
    def __init__(self,currentdir):
        self.currentDir = currentdir

    def findfile(self,req_file_size):
        queue = self.currentDir.children
        while(queue):
            currentD = queue.pop(0)
            if currentD is not None and (len(currentD.files) > 0 or currentD.children is not None):
                for file in currentD.files:
                    if file.filesize == req_file_size:
                        return f"File found {file.filename}"
                    
                queue += currentD.children

        return f"File with the appropriate file size not found!!!!"
    
if __name__ == '__main__':
    spark = Directory("Spark",1000,None,None)
    spark.files = [File("Spark_core",200,spark),File("Spark_sql",100,spark)]
    root = Directory("InterviewPrep",1000,None,spark)
    root.files = [File("Resume",10,root)]
    root.children = [spark]
                
            
    fs = Filesystem(root)
    print(fs.findfile(200))