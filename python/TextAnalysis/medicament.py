import json

class Medicament:


    def __init__(self, name = "", dosage = 0, form = "", frequency = "", duration = ""):
        self.name = name
        self.dosage = dosage
        self.form = form
        self.frequency = frequency
        self.duration = duration

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def setForm(self, form):
        self.form = form

    def setName(self, name):
        self.name = name

    def setFrequency(self, frequency):
        self.frequency = frequency

    def setDosage(self, dosage):
        self.dosage = dosage

    def setDuration(self, duration):
        self.duration = duration