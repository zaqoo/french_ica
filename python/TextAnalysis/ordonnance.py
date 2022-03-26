import json

class Ordonance:
    def __init__(self, patient = None):
        self.medicaments = []
        self.patient = patient

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def addMedicament(self, med):
        self.medicaments.append(med)

    def setPatient(self, patient):
        self.patient = patient
