from ordonnance import *
from medicament import *
from patient import *

patient = Patient("FISHER", "California Bitch")
med1 = Medicament("DOLIPRANE", 500, "cachet", "3 fois par jour")
ordonance = Ordonance(patient)
ordonance.addMedicament(med1)



print(ordonance.toJSON())