# 1) Escreva uma função recursiva que calcule o fatorial de um número.
def fatorial(n: int) -> int:
    """Essa função recebe um número e retorna 
    o fatorial dele, chamando ela mesmo n vezes
    e sempre subtraindo 1"""
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)

# 2) Desenvolva uma função recursiva que calcule a soma dos números de 1 a n.
def soma(n: int) -> int:
    """Essa função chama ela mesma n - 1 vezes e
    vai somando os valores até o n ser 1"""
    if n == 1:
        return 1
    else:
        return n + soma(n - 1)

# 3) Faça uma função recursiva que calcule o n-ésimo número da sequência de Fibonacci.
def fibonacci(n: int) -> int:
    """Essa função recebe um número e chama ela mesma
    várias vezes para calcular a soma dos dois números
    anteriores na sequência"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 4) Escreva uma função recursiva que verifique se uma palavra é um palíndromo.
def palindromo(palavra: str) -> bool:
    """Essa função recebe uma palavra e verifica se 
    a primeira e a última letras são iguais, depois ela
    remove as letras e chama ela mesma de novo."""
    if len(palavra) <= 1:
        return True
    elif palavra[0] == palavra[-1]:
        return palindromo(palavra[1:-1])
    else:
        return False

# 5) Desenvolva uma função recursiva que inverta uma string.
def inverte_string(s: str) -> str:
    """Essa função recebe uma string e vai somando
    as últimas letras da string enquanto a função 
    chama ela mesma até dar o tamanho da string"""
    if len(s) <= 1:
        return s
    else:
        return s[-1] + inverte_string(s[:-1])

# 6) Escreva uma função recursiva que conte o número de dígitos de um número inteiro.
def conta_digitos(n: int) -> int:
    """Essa função recebe um número inteiro e chama
    ela mesma dividindo ela por dez e somando 1 até 
    o valor absoluto dela for menos que 10"""
    if abs(n) < 10:
        return 1
    else:
        return 1 + conta_digitos(n // 10)

# 7) Crie uma função recursiva que calcule a soma dos elementos de um vetor.
def soma_vetor(vetor: list) -> int:
    """Essa função recebe uma lista e soma o 
    primeiro elemento com o restante da lista 
    chamando ela mais uma vez."""
    if len(vetor) == 0:
        return 0
    else:
        return vetor[0] + soma_vetor(vetor[1:])

# 8) Desenvolva uma função recursiva que encontre o maior elemento de um vetor.
def maior_elemento(vetor: list) -> int:
    """Essa função recebe um vetor e pega o primeiro
    elemento dela, depois ela chama ela mesma e compara
    o primeiro elemento com os outros para decidir o maior."""
    if len(vetor) == 1:
        return vetor[0]
    else:
        maior_resto = maior_elemento(vetor[1:])
        return vetor[0] if vetor[0] > maior_resto else maior_resto

# 9) Escreva uma função recursiva que calcule a potência de um número (base elevada ao expoente).
def potencia(base: int, expoente: int) -> int:
    """Essa função recebe uma base e um expoente e
    se o expoente for menor que zero ela chama ela mesma
    para calcular a potência sob um, caso não, ela 
    multiplica a base e chama ela mesma expoente vezes"""
    if expoente == 0:
        return 1
    elif expoente < 0:
        return 1 / potencia(base, -expoente)
    else:
        return base * potencia(base, expoente - 1)

# 10) Faça uma função recursiva que resolva o problema das Torres de Hanói para n discos.
def torres_de_hanoi(n: int, origem: str, destino: str, auxiliar: str):
    """Uma função bem complicada..."""
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else:
        torres_de_hanoi(n - 1, origem, auxiliar, destino)
        print(f"Mova o disco {n} de {origem} para {destino}")
        torres_de_hanoi(n - 1, auxiliar, destino, origem)
