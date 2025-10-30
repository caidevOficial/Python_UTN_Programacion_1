import json

with open('./personas.json', 'r', encoding='utf-8') as file:
    configs = json.load(file)



personas = configs.get('nombres')

personas.append({"nombre": 'Coqui', "apellido": 'Argento'})
print(personas)
    

with open('./personas.json', 'w', encoding='utf-8') as file:
    json.dump(configs, file, indent=4)
