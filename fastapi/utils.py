
import json

class Utils:
    def __init__(self):
        self.json_data = self.load_json()

    def load_json(self):
        with open("patients.json","r") as f:
            data = json.load(f)
        return data

