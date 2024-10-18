# 1) Escreva um programa que leia uma matriz 3x3 e imprima a soma dos elementos da diagonal principal.
def somadiagonalprincipal(m: list[list]) -> int:
    """Essa função recebe uma matriz 3x3 e retorna
    a soma da sua diagonal principal"""
    dp = []
    for i in range(len(m)):
        for j in range(len(m)):
            if i == j:
                dp.append(m[i][j])
    return sum(dp)

assert somadiagonalprincipal([[1,2,3], [4,5,6], [7,8,9]]) == 15

# 2) Desenvolva um algoritmo que leia uma matriz 3x3 e imprima a soma dos elementos da diagonal secundária.
def somadiagonalsecundaria(m: list[list]) -> int:
    """Essa função recebe uma matriz 3x3 e retorna
    a soma da sua diagonal secundária"""
    soma = 0
    for i in range(len(m)):
        soma += m[i][2 - i]
    return soma

assert somadiagonalsecundaria([[1,2,3], [4,5,6], [7,8,9]]) == 15

# 3) Faça um programa que leia duas matrizes 3x3 e gere uma terceira matriz que seja a soma das duas primeiras.
def somadematrizes(m1: list[list], m2: list[list]) -> list[list]:
    """Essa função soma duas matrizes 3x3"""
    soma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Matriz 3x3 vazia
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            soma[i][j] = m1[i][j] + m2[i][j]
    return soma

assert somadematrizes([[1,2,3], [4,5,6], [7,8,9]], 
                      [[-1,-2,-3], [-4,-5,-6], [-7,-8,-9]]) == [[0,0,0],[0,0,0],[0,0,0]]

# 4) Escreva um programa que leia uma matriz 3x3 e encontre o maior e o menor valor armazenados na matriz.
def maioremenormatriz(m: list[list]) -> tuple:
    """Essa função encontra o maior e o menor elemento
    de uma matriz 3x3"""
    maior = float("-inf")
    menor = float("inf")

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > maior:
                maior = m[i][j]
            if m[i][j] < menor:
                menor = m[i][j]

    return (menor, maior)

assert maioremenormatriz([[1,2,3], [4,5,6], [7,8,9]]) == (1,9)

# 5) Desenvolva um algoritmo que leia uma matriz 3x3 e calcule a média dos elementos armazenados na matriz.
def mediadamatriz(m: list[list]) -> float:
    """Essa função recebe uma matriz 3x3 e devolve a
    média dos elementos dessa matriz"""
    soma = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            soma += m[i][j]

    return (soma / (3*3))

assert mediadamatriz([[1,2,3], [4,5,6], [7,8,9]]) == 5

# 6) Escreva um programa que leia uma matriz 3x3 e substitua todos os números negativos por zero.
def matrizpositivosouzero(m: list[list]) -> list[list]:
    """Essa função recebe uma matriz 3x3 e subistitui
    todos os números negativos dela por zero"""
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] < 0:
                m[i][j] = 0
    return m

assert matrizpositivosouzero([[-1,2,-3], [4,5,-6], [7,8,-9]]) == [[0,2,0], [4,5,0], [7,8,0]]

# 7) Crie um programa que leia duas matrizes 3x3 e gere uma terceira matriz que seja a multiplicação das duas primeiras.
def multiplicaodematrizes(m1: list[list], m2: list[list]) -> list[list]:
    """Essa função multiplica duas matrizes 3x3"""
    m3 = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(3):
        for j in range(3):
            m3[i][j] = m1[i][j] * m2[i][j]
    
    return m3

assert multiplicaodematrizes([[1,2,3], [4,5,6], [7,8,9]], 
                      [[-1,-2,-3], [-4,-5,-6], [-7,-8,-9]]) == [[-1,-4,-9],[-16,-25,-36],[-49,-64,-81]]

# 8) Desenvolva um algoritmo que leia uma matriz 3x3 e imprima a matriz transposta.
def matriztransposta(m: list[list]) -> list[list]:
    """Essa função recebe uma matriz e retona ela transposta"""
    transposta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            transposta[i][j] = m[j][i]
    return transposta

assert matriztransposta([[1,2,3], [4,5,6], [7,8,9]]) == [[1,4,7], [2,5,8], [3,6,9]]

# 9) Escreva um programa que leia uma matriz 3x3 e verifique se ela é simétrica.
def matrizsimetrica(m: list[list]) -> bool:
    """Essa função recebe uma matriz 3x3 e verifica
    se a matriz é simétrica"""
    for i in range(3):
        for j in range(3):
            if m[i][j] != m[j][i]:
                return False
    return True

assert matrizsimetrica([[1,2,3], [2,5,6], [3,6,9]]) == True

# 10) Faça um programa que leia uma matriz 3x3 e calcule o determinante da matriz
def determinantematriz(m: list[list]) -> float:
    """Essa função calcula o determinante de uma 
    matriz 3x3"""
    det = (m[0][0] * m[1][1] * m[2][2] +
           m[0][1] * m[1][2] * m[2][0] +
           m[0][2] * m[1][0] * m[2][1]) - \
          (m[0][2] * m[1][1] * m[2][0] +
           m[0][1] * m[1][0] * m[2][2] +
           m[0][0] * m[1][2] * m[2][1])
    
    return det

assert determinantematriz([[1,2,3], [0,1,4], [5,6,0]]) == 1
