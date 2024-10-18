# 1) Escreva um programa que leia 10 números e armazene em um vetor. 
# Em seguida, imprima os números na ordem inversa.
def ordemreversa(l: list) -> list:
    """Essa função recebe 10 números e imprime
    eles em ordem reversa"""
    vetor = sorted(l, reverse=True)
    return vetor

assert ordemreversa([1,2,3,4,5,6,7,8,9,10]) == [10,9,8,7,6,5,4,3,2,1]

# 2) Desenvolva um algoritmo que leia um vetor de 10 posições e 
# calcule a soma dos elementos armazenados no vetor.
def somavetor(vetor: list) -> int:
    """Essa função recebe um vetor de 10 elementos
    e retorna a soma dos elementos"""

    return sum(vetor)

assert somavetor([48,56,14,25,17,87,69,34,55,104])

# 3) Faça um programa que leia dois vetores de 5 posições e gere um 
# terceiro vetor que seja a soma dos dois primeiros.
def somavetores(x: list, y:list) -> int:
    """Essa função recebe dois vetores de cinco
    elementos e retorna a soma deles"""
    assert len(x) == len(y)
    return [i + j for i, j in zip(x, y)]

assert somavetores([1,2,3,4,5], [6,7,8,9,10]) == [7,9,11,13,15]

# 4) Escreva um programa que leia um vetor de 10 posições e encontre 
# o maior e o menor valor armazenados no vetor.
def maioremenor(vetor: list):
    """Essa função recebe um vetor de dez elementos e retorna
    o maior e o menor elemento"""
    i, j = max(vetor), min(vetor)
    return i,j

assert maioremenor([1,2,3,4,5,6,7,8,9,10]) == (10, 1)

# 5) Desenvolva um algoritmo que leia um vetor de 10 posições e conte
# quantos números pares e ímpares estão armazenados no vetor.
def pareseimpares(vetor: list):
    """Essa função recebem um vetor de dez
    elementos e retorna duas listas, uma com
    os números pares e outra com os ímpares"""
    p = [i for i in vetor if i%2 == 0]
    i = [i for i in vetor if i%2 != 0]
    return (p, i)

assert pareseimpares([1,2,3,4,5,6,7,8,9,10]) == ([2,4,6,8,10], [1,3,5,7,9])

# 6) Escreva um programa que leia um vetor de 10 posições e substitua
# todos os números negativos por zero.
def positivose0(vetor: list) -> list:
    """Essa função recebe um vetor de dez elementos
    e retorna 0 no lugar dos elementos negativos"""
    vetor = [0 if i < 0 else i for i in vetor]
    return vetor

assert positivose0([-1,-2,-3,-4,-5,1,2,3,4,5]) == [0,0,0,0,0,1,2,3,4,5]

# 7) Crie um programa que leia dois vetores de 10 posições e gere um
# terceiro vetor que contenha os elementos comuns aos dois vetores.
def elementosemcomum(vetor1: list, vetor2: list) -> list:
    """Essa função recebe dois vetores de dez elementos
    e retorna uma lista com os elementos em comum delas"""
    eec = [i for i in vetor1 if i in vetor2]
    return eec

assert elementosemcomum([1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,8,6,9,1]) == [1,6,8,9]

# 8) Desenvolva um algoritmo que leia um vetor de 10 posições e remova
# os elementos duplicados.
def removeduplicados(vetor: list) -> list:
    """Essa função remove os elementos duplicados em um vetor"""
    vetorsemduplicados = []
    for i in vetor:
        if not i in vetorsemduplicados:
            vetorsemduplicados.append(i)
    return vetorsemduplicados

assert removeduplicados([1,1,1,1,2,3,8,9,8,3]) == [1,2,3,8,9]

# 9) Escreva um programa que leia um vetor de 10 posições e ordene os
# elementos em ordem crescente.
def ordena(vetor: list) -> list:
    """Essa função recebe um vetor e ordena ele em ordem crescente"""
    return sorted(vetor)

assert ordena([5,7,6,9,1,3,4,8,2,10]) == [1,2,3,4,5,6,7,8,9,10]

# 10) Faça um programa que leia um vetor de 10 posições e calcule a
# média dos elementos. Em seguida, imprima todos os elementos que estão acima da média.
def acimadamedia(vetor: list) -> list:
    """Essa função recebe um vetor, calcula a média dele e
    retorna os elementos acima da média"""
    media = sum(vetor) / len(vetor)
    return [i for i in vetor if i > media]

assert acimadamedia([1,2,3,4,5,6,7,8,9,10]) == [6,7,8,9,10]