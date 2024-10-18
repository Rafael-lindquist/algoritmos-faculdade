# arquivo = open("nome", "modo")

# for linha em arquivo:

# modos: 'r', 'w', 'a', 'a+'

# arquivo.seek(bytes)
nome_arquivo = input("Digite o nome do arquivo: ")

with open(nome_arquivo, 'w') as arquivo:
    while True:
        conteudo = input("Digite (ou /exit para encerrar): ")

        if conteudo == '/exit':
            break

        arquivo.write(f"{conteudo}\n")

with open(nome_arquivo, 'r') as arquivo:
    print("Conteudo do arquivo: \n")
    print(arquivo.read())
