import json

class Medicament:
    def __init__(self, name, dosage, form, frequency):
        self.name = name
        self.dosage = dosage
        self.form = form
        self.frequency = frequency

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)