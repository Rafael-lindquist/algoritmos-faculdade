import json

def aumenta_salario_departamento(departamento: str, percentual: float):
    
    with open("funcionarios.json", 'r') as file:
        dados = json.load(file)

    desconto = 1 + percentual

    for i in dados:
        if i['departamento'] == departamento:
            i['salario'] *= desconto
        print(i["salario"])

    with open("funcionarios.json", 'w') as file:
        json.dump(dados, file)

aumenta_salario_departamento("RH", 0.1)



    