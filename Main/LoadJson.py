import json

class loadJson:
    def __init__(self, file):
        self.file = file
        with open(self.file) as res:
            print(f"Loaded '{file}' successfully!")
            self.data = json.load(res)