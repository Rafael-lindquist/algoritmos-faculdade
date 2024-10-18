# 1) Escreva um programa que leia um número e verifique se ele é positivo, negativo ou zero.
def verifica_numero(num: float) -> str:
    """Esse programa retorna positivo, negativo ou zero 
    baseado em um número"""
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "zero"
    
assert verifica_numero(8) == "positivo", "a função não funcionou"
assert verifica_numero(0) == "zero", "a função não funcionou"
assert verifica_numero(-8) == "negativo", "a função não funcionou"

# 2) Crie um programa que determine se um número é par ou ímpar.

def verifica_numero(num: float) -> str:
    """Essa função recebe um núemro e verifica se é par ou ímpar"""

    return "par" if num % 2 == 0 else "impar"
    
assert verifica_numero(4) == "par"
assert verifica_numero(5) == "impar"

# 3) Desenvolva um algoritmo que leia três números e imprima o maior deles.

def tresnumeros(num1: int, num2:int, num3:int) -> int:
    """Essa função recebe e devolve o maior deles"""

    return max(num1, num2, num3)

tresnumeros(-4, 8, 0) == 8

# 4) Escreva um programa que verifique se um ano é bissexto.

def anobissexto(str: str) -> bool:
    """Essa função recebe uma string com um ano e retorna
    True caso o ano seja bissexto e False caso o ano não
    seja bissexto"""

    ud = int(str[-2:])
    if ud % 4 == 0 or ud % 400 == 0:
        return True
    else:
        return False
    
assert anobissexto("2000") == True
assert anobissexto("1988") == True
assert anobissexto("2017") == False

# 5) Faça um programa que leia dois números e mostre o maior. Se forem iguais, informe que são iguais.

def comparacao(num1: int, num2: int):
    """Essa função recebe dois números e retorna o maior deles,
    caso sejam iguais retorna que são iguais"""

    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "os números são iguais"
    
assert comparacao(10, 12) == 12
assert comparacao(0, 0) == "os números são iguais"

# 6) Desenvolva um algoritmo que leia a idade de uma pessoa e informe se ela é menor de idade (menos de 18 anos), 
# maior de idade (entre 18 e 64 anos) ou idosa (65 anos ou mais).

def classificaidade(idade: int) -> str:
    """Essa função recebe uma idade (int) e classifica essa idade
    como sendo menor de idade, maior de idade ou idoso."""

    if idade > 0 and idade < 18:
        return "menor de idade"
    elif idade >= 18 and idade < 64:
        return "maior de idade"
    elif idade >= 64:
        return "idoso"
    else: 
        return "valor invalido"
    
assert classificaidade(17) == "menor de idade"
assert classificaidade(34) == "maior de idade"
assert classificaidade(68) == "idoso"
assert classificaidade(-1) == "valor invalido"

# 7) Escreva um programa que calcule a média de três notas e determine se o aluno está aprovado (média maior ou igual a 6),
# em recuperação (média entre 4 e 5.9) ou reprovado (média menor que 4).

def aprovado(nota1: float, nota2: float, nota3: float) -> str:
    """Essa função recebe três notas e retorna se o aluno foi 
    aprovado , reprovado ou está em recuperação."""

    media = (nota1 + nota2 + nota3) / 3
    if media >= 6:
        return "aprovado"
    elif media < 6 and media >= 4:
        return "em recuperação"
    else:
        return "reprovado"
    
assert aprovado(8, 9, 10) == "aprovado"
assert aprovado(5, 4, 6) == "em recuperação"
assert aprovado(2, 0, -1) == "reprovado"

# 8) Crie um programa que leia o nome, idade e sexo de uma pessoa e determine se ela pode se aposentar 
# (homens a partir de 65 anos, mulheres a partir de 60 anos).

def inss(nome: str, idade: int, sexo: str) -> bool:
    """Essa função recebe o nome, a idade e o sexo de uma pessoa
    retorna True caso a pessoa possa se aponsentar ou False caso
    a pessoa não possa se aponsentar"""

    if sexo == 'masculino' and idade >= 65:
        return True
    elif sexo == 'feminino' and idade >= 60:
        return True
    else: 
        return False
    
assert inss('Rafael', 19, 'masculino') == False
assert inss('Palmeiras', 111, 'feminino') == True

# 9) Desenvolva um algoritmo que simule um caixa eletrônico, onde o usuário informe o valor a ser sacado
# e o programa exiba a quantidade de notas de 100, 50, 20, 10, 5 e 1 necessárias para o saque.

def caixaeletronico(valor: int) -> dict:
    """Essa função recebe um valor a ser sacado e retorna um dicionário
    com quantas notas serão necessária e quais valores das notas"""
    notas = [100, 50, 20, 10, 5, 1]
    numnotas = {}
    for nota in notas:
        quantidade = valor // nota
        valor %= nota
        numnotas[nota] = quantidade
    return numnotas

print(caixaeletronico(199))

# 10) Escreva um programa que leia três lados de um triângulo e verifique se eles formam um triângulo válido.
#  Se for válido, determine se é equilátero, isósceles ou escaleno.

def triangulo(a: float, b: float, c: float) -> bool:
    """Essa função retorna equilátero, isósceles ou escaleno 
    caso os lados formem um triângulo e False caso os lados do
    triângulo não formem um triângulo"""

    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)) or (a == 0) or (b == 0) or (c == 0):
        return False
    
    else: 
        if a == b == c:
            return "equilatero"
        elif a != b  and b != c and a != c:
            return "escaleno"
        else: 
            return "isoceles"
    
assert triangulo(5, 5, 5) == 'equilatero'
assert triangulo(5, 8, 5) == "isoceles"
assert triangulo(3, 4, 5) == "escaleno"
assert triangulo(0, 0, 0) == False
assert triangulo(1, 2, 40) == False 