import csv

# 1) Escreva um programa que leia um arquivo de texto e conte o número de palavras.
def le_arquivo_de_textp(arquivo: str) -> int:
    """Essa função recebe o nome de um arquivo .txt 
    e conta o número palavras que tem nele"""
    with open(arquivo, 'r') as f:
        texto = f.read()
        num = len(texto.split())
        return num

# 2) Desenvolva um algoritmo que leia um arquivo de texto e conte o número de linhas.
def conta_linhas_arquivo(arquivo: str) -> int:
    """Essa função recebe o nome de um arquivo .txt
    e conta o número de linhas nele"""
    with open(arquivo, 'r') as f:
        num = sum([1 for linha in f])
        return num

# 3) Faça um programa que leia um arquivo de texto e imprima o conteúdo invertido (da última linha para a primeira).
def inverte_arquivo(arquivo: str):
    """Essa função recebe o nome de um arquivo .txt 
    e inverte a ordem das palavras nele."""
    with open(arquivo, 'r') as f:
        texto = f.read()
        texto = texto.split()[::-1]
        texto = ' '.join(texto)
        print(texto)

# 4) Escreva um programa que leia um arquivo de texto e imprima todas as palavras que começam com uma determinada letra.
def imprime_palavras_selecionadas(arquivo: str, letra: str):
    """Essa função recebe o nome de um arquivo .txt 
    e imprime as palavras que começam com 
    uma determinada letra."""
    with open(arquivo, 'r') as f:
        texto = f.read()
        texto = texto.split()
        for i in texto:
            if i[0] == letra:
                print(texto)

# 5) Desenvolva um algoritmo que leia um arquivo de texto e crie um novo arquivo apenas com as linhas que contêm um determinado palavra.
def arquivo_com_linhas_selecionadas(arquivo: str, palavra: str):
    """Essa função recebe o nome de um arquivo .txt 
    e cria outro arquivo com as linhas do primeiro 
    arquivo que tem determinada palavra."""
    with open(arquivo, 'r') as f:
            linhas = [linha for linha in f if palavra in linha]
        
    with open(arquivo, 'w') as novo_arquivo:
        novo_arquivo.writelines(linhas)

# 6) Escreva um programa que leia um arquivo CSV e imprima o conteúdo na forma de uma tabela.
def de_cvs_para_tabela(arquivo: str):
    """Essa função recebe o nome de um arquivo .csv 
    e imprime o conteúdo em dorma de uma tabela."""
    pass 


# 7) Crie um programa que leia um arquivo CSV e calcule a média dos valores de uma coluna específica.
def media_coluna_arquiv_csv(arquivo: str, nome_coluna:str):
    """Essa função recebe o nome de um arquivo csv
    e calcula a média dos valores de uma coluna específica"""
    valores = []
    with open(arquivo, newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            valor = float(linha[nome_coluna])
            valores.append(valor)

    if valores:
        media = sum(valores) / len(valores)
        return media
    else:
        return None


# 8) Desenvolva um algoritmo que leia um arquivo CSV e crie um novo arquivo apenas com as linhas que atendem a um determinado critério.
def linhas_csv_determinadas(arquivo: str, arquivo_saida: str, nome_coluna: str, criterio):
    """Essa função recebe o nome de um arquivo csv e 
    cria outro arquivo com as linhas do primeiro 
    arquivo que atemdem a um determinado critério."""
    with open(arquivo, newline='', encoding='utf-8') as arquivo_csv_entrada:
        leitor_csv = csv.DictReader(arquivo_csv_entrada)
        linhas_filtradas = [linha for linha in leitor_csv if criterio(linha[nome_coluna])]

        if linhas_filtradas:
            with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as arquivo_csv_saida:
                campos = leitor_csv.fieldnames        
                escritor_csv = csv.DictWriter(arquivo_csv_saida, fieldnames=campos)
                escritor_csv.writeheader()
                escritor_csv.writerows(linhas_filtradas)

            return arquivo_saida
        

# 9) Escreva um programa que leia dois arquivos de texto e crie um terceiro arquivo que seja a combinação dos dois primeiros.
def soma_de_arquivos(arquivo1: str, arquivo2: str): 
    """Essa função recebe o nome de dois arquivos e cria um 
    terceiro arquivo com o conteudo dos outros dois."""
    with open(arquivo1, 'r') as arq1:
        conteudo1 = arq1.read()

    with open(arquivo2, 'r') as arq2:
        conteudo2 = arq2.read()

    arquivo3 = conteudo1 + "\n" + conteudo2

    with open("arquivo3.txt", 'w') as f:
        f.write(arquivo3)

# 10) Faça um programa que leia um arquivo binário e imprima o conteúdo em hexadecimal.
def de_binario_para_hexadecimal(arquivo:str):
    """Essa função recebe o nome de um arquivo, lê
    esse arquivo em binário, transforma o conteudo 
    desse arquivo para hexadecimal e imprime."""
    with open(arquivo, 'rb') as f:
            while True:
                bloco = f.read(16) # 16 bytes
                if not bloco:
                    break
                print(' '.join(f'{byte:02x}' for byte in bloco))
