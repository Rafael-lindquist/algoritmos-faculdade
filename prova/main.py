def calcula_total_por_produto(transacoes):
    total_por_produto = {}
    for transacao in transacoes:
        produto = transacao["produto"]
        quantidade = transacao["quantidade"]
        preco_unitario = transacao["preco_unitario"]
        total = quantidade * preco_unitario
        if produto in total_por_produto:
            total_por_produto[produto] += total
        else:
            total_por_produto[produto] = total
    return total_por_produto
