from ordonnance import *
from medicament import *
from patient import *
from analyse import *

patient = Patient("FISHER", "California Bitch")
med1 = Medicament("DOLIPRANE", 500, "cachet", "3 fois par jour")
exam = Examination("Analyse d'urine")
ordonance = Ordonance(patient)
ordonance.addMedicament(med1)
ordonance.addMedicament(exam)

print(ordonance.toJSON())

medList = ordonance.getMedicaments()
medList[0].setForm("pills")
print(ordonance.toJSON())

analyse_input(["Good Mr Mickael Jones, I think your joint pain is due to a gout attack. I think it will be necessary, it will be necessary to prescribe cortisone I would say Solu. At a rate of 60 mg, In the morning for 7 days and then we see each other if there is any problem."])
#analyse_input(["Good Mr Bertrand, I think your joint pain is due to a gout attack. I think it will be necessary, it will be necessary to prescribe cortisone I would say Solu. At a rate of 60 mg, In the morning for 7 days and then we see each other if there is any problem."])