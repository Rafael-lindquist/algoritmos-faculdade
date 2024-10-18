# 1. Escreva um programa que imprima os números de 1 a 100.
def numeros1a100():
    """Essa função imprime os números de 1 a 100"""
    for i in range(1, 101):
        print(i)
numeros1a100()

# 2. Desenvolva um algoritmo que imprima a tabuada de um número fornecido pelo usuário.
def tabuada(n: int):
    """Essa função imprime a tabuada de um número fornecido"""
    for i in range(1, 11):
        print(i * n)
tabuada(7)

# 3. Faça um programa que leia 10 números e imprima a média deles.
def media10(l: list) -> float:
    """Essa função lê dez números e imprime a média deles"""
    assert len(l) == 10, "a lista deve ter 10 números"
    return (sum(l) / len(l))

assert media10([1,2,3,4,5,6,7,8,9,10]) == 5.5

# 4. Escreva um programa que leia um número inteiro positivo e calcule o seu fatorial.
def fatorial(n: int) -> int:
    """Essa função retorna o fatorial de um número dado"""
    soma = 1
    while n > 0:
        soma *= n
        n -= 1
    return soma

assert fatorial(5) == 120

# 5. Desenvolva um algoritmo que leia um número inteiro e determine se ele é primo.
def primo(n: int) -> bool:
    """Essa função recebe um número e retorna True se ele for primo,
    senão retorna False"""
    if n < 0:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
    return True

assert primo(17) == True
assert primo(2) == True
assert primo(42) == False

# 6. Escreva um programa que imprima os números pares entre 1 e 50.
def pares1a50():
    """Essa função imprime os números pares de 1 a 50"""
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)
pares1a50()

# 7. Crie um programa que leia um número n e imprima os n primeiros números da sequência de Fibonacci.
def fibonacci(n: int):
    """Essa função impreme os n primeiros números da 
    sequência de fibonacci começando no número n"""
    seq = [n, n]
    for i in range(n):
        seq.append(seq[-1] + seq[-2])
    return seq

assert fibonacci(5) == [5, 5, 10, 15, 25, 40, 65]

# 8. Desenvolva um algoritmo que simule um jogo de adivinhação, onde o usuário deve adivinhar
# um número entre 1 e 100 gerado pelo programa. O programa deve informar se o palpite é maior
# ou menor que o número gerado.
from random import randint
def adivinhanum(n: int) -> str:
    """Esse algoritmo informa se o palpite é maior ou menor 
    que o número gerado entre 1 a 100"""
    num = randint(1, 100)
    if n > num:
        return "O palpite é maior que o número"
    if n < num:
        return "O palpite é menor que o número"
    
print(adivinhanum(47))

# 9. Escreva um programa que leia um número inteiro e imprima os seus divisores.
def divisores(n: int):
    """Essa função recebe um número e imprime uma 
    lista com todos os divisores desse número"""
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    print(div)

divisores(360)

# 10. Faça um programa que leia um número inteiro positivo n e imprima todos os números primos entre 1 e n.
def primos(n: int):
    """Essa função recebe um número e imprime todos
    os números primos até esse número"""
    primos = []
    for i in range(1, n+1):
        if primo(i):
            primos.append(i)
    print(primos)

primos(50)