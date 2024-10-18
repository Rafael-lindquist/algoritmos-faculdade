# 1) Escreva uma função que receba um número inteiro e retorne se ele é par ou ímpar.
def parouimpar(num:int) -> bool:
    """Essa função recebe um número e retorna
    se esse número é par ou ímpar"""
    return True if num % 2 == 0 else False

assert parouimpar(8) == True
assert parouimpar(7) == False

# 2) Desenvolva uma função que receba um número inteiro e retorne o seu fatorial.
def fatorial(n: int) -> int:
    """Essa função retorna o fatorial de um número dado"""
    soma = 1
    while n > 0:
        soma *= n
        n -= 1
    return soma

assert fatorial(6) == 720

# 3) Faça uma função que receba três números e retorne o maior deles.
def maiordetres(num1: int, num2: int, num3: int) -> int:
    """Essa função recebe três números e retorna o maior deles"""
    return max(num1, num2, num3)

assert maiordetres(1,2,3) == 3

# 4) Escreva uma função que receba um vetor de números e retorne a média dos elementos.
def media(vetor: list) -> float:
    """Essa função recebe um vetor e retorna a média 
    dos números deles"""
    return sum(vetor)/len(vetor)

assert media([40, 80, 120, 160, 200]) == 120.0

# 5) Desenvolva uma função que receba um vetor de números e retorne a soma dos elementos.
def somavetores(x: list, y:list) -> int:
    """Essa função recebe dois vetores de cinco
    elementos e retorna a soma deles"""
    assert len(x) == len(y)
    return [i + j for i, j in zip(x, y)]

assert somavetores([1,2,3,4,5], [6,7,8,9,10]) == [7,9,11,13,15]

# 6) Escreva uma função que receba dois números e retorne o maior divisor comum (MDC) entre eles.
def mdc(num1: int, num2:int) -> int:
    """Essa função recebe dois números e retorna o MDC deles"""
    menor = min(num1, num2)
    for i in range(menor, (num1*num2) + 1):
        return i if (i % num1) == 0 and (i % num2)== 0 else num1*num2
    
assert mdc(2, 11) == 22

# 7) Crie uma função que receba um número inteiro positivo n e retorne os n primeiros números da sequência de Fibonacci.
def fibonacci(n: int):
    """Essa função impreme os n primeiros números da 
    sequência de fibonacci começando no número n"""
    seq = [n, n]
    for i in range(n):
        seq.append(seq[-1] + seq[-2])
    return seq

assert fibonacci(7) == [7, 7, 14, 21, 35, 56, 91, 147, 238]

# 8) Desenvolva uma função que receba um número inteiro e retorne se ele é primo.
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

# 9) Escreva uma função que receba um vetor de números e retorne o vetor ordenado em ordem crescente.
def ordena(vetor: list) -> list:
    """Essa função recebe um vetor e ordena ele em ordem crescente"""
    return sorted(vetor)

assert ordena([5, 3, 1, 4, 2]) == [1,2,3,4,5]

# 10) Faça uma função que receba uma matriz 3x3 e retorne a matriz transposta.
def matriztransposta(m: list[list]) -> list[list]:
    """Essa função recebe uma matriz e retona ela transposta"""
    transposta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            transposta[i][j] = m[j][i]
    return transposta

assert matriztransposta([[1,2,3], [4,5,6], [7,8,9]]) == [[1,4,7], [2,5,8], [3,6,9]]