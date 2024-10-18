import json

with open("dados.json", encoding="utf-8") as file:
    dados = json.load(file)

print(dados)
dicionario = {
    "prova1": 10,
    "prova2": 10,
    "projeto": 10,
}

with open("dados.json", "a+", encoding="utf-8") as file:
    file.write(json.dumps(dicionario))