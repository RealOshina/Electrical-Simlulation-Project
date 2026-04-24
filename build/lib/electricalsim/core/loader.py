import json

class Loader:
    def open_file(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return data