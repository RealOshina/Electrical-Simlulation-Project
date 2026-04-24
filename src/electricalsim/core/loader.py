import json

class Loader:
    def open_file(filepath):
        with open(filepath, "r") as file:
            data = json.load(file)
        return data