class FileManager:

    def __init__(self, filename, mode) -> None:
        print("object created")
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("object entered")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("object exited")
        self.file.close()


with FileManager("operateme.log", "w") as f:
    f.write("ContextManager")


print(f.closed)
