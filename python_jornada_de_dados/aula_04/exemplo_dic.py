import json

produto_01 = {
    "nome": "Sapato",
    "quantidade": 10,
    "preco": 7.5,
    "disponibilidade": True
}

produto_02 = {
    "nome": "Camiseta",
    "quantidade": 20,
    "preco": 15.0,
    "disponibilidade": True
}

#print(produto_01["nome"])

carrinho: list = []
carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)