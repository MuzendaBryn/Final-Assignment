from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data)

# Example usage
text_handler = TextFileHandler("example.txt")
binary_handler = BinaryFileHandler("example.bin")

text_handler.write("Hello, world!")
print(text_handler.read())  # Output: Hello, world!

binary_handler.write(b'\x00\x01\x02\x03')
print(binary_handler.read())  # Output: b'\x00\x01\x02\x03'
