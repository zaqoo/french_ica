from jinja2 import Environment, FileSystemLoader
import os
     
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')
     
     
filename = os.path.join(root, 'html', 'index.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        doctor_name = "Dr. Guillaume CUMY",
        patient_name = "Fabrice VIOT",
        medic = [["Doliprane", "500mg", "3x/jour"], ["Spasphon", "100mg", "2x jour"]]
    ))