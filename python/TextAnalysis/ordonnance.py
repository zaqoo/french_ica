import json

class Ordonance:
    def __init__(self, patient = None):
        self.medicaments = []
        self.patient = patient
        self.prescripteur = "Guillaume CUNY"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def addMedicament(self, med):
        self.medicaments.append(med)

    def setPatient(self, patient):
        self.patient = patient

    def getMedicaments(self):
        return self.medicaments

    def getMedIndex(self, name):
        for i in range(len(self.medicaments)):
            if self.medicaments[i].name == name:
                return i
