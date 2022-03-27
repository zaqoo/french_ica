import json

class Patient:
    def __init__(self, name, address = ""):
        self.name = name
        self.address = address

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
