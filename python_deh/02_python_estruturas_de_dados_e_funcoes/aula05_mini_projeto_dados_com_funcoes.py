# Gerenciar uma pequena lista de produtos, com:
# nome, preço e categoria

#Vamos:
# - Cadastrar produtos
# - calcular valor total
# - Filtrar por categoria
# - calcular média de preços

def criar_produto(nome, preco, categoria):
    return {
        'nome': nome,
        'preco': float(preco),
        'categoria': categoria
    }

def adicionar_produto(lista, produto):
    lista.append(produto)

def calcular_valor_total(lista):
    total = 0
    for produto in lista:
        total += produto['preco']
    return total 

def filtrar_por_categoria(lista, categoria):
    filtrados = []
    for produto in lista:
        if produto['categoria'] == categoria:
            filtrados.append(produto)
    return filtrados

def calcular_media_precos(lista):
    if len(lista) == 0:
        return 0
    total = calcular_valor_total(lista)
    return total / len(lista)

def exibir_produtos(lista):
    if not lista:
        print("Nenhum produto encontrado.")
        return

    for produto in lista:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Categoria: {produto['categoria']}")

# Exemplo de uso
produtos = []

adicionar_produto(produtos, criar_produto('Camiseta', 50, 'Roupas'))
adicionar_produto(produtos, criar_produto('Calça', 100, 'Roupas'))
adicionar_produto(produtos, criar_produto('Tênis', 150, 'Calçados'))

print('Lista de produtos:')
exibir_produtos(produtos)

total = calcular_valor_total(produtos)
print(f'Valor total dos produtos: {total}')
media = calcular_media_precos(produtos)
print(f'Média de preços dos produtos: {media}')

categoria_filtrada = 'Roupas'
produtos_filtrados = filtrar_por_categoria(produtos, categoria_filtrada)

print(f'Produtos na categoria "{categoria_filtrada}":')
exibir_produtos(produtos_filtrados) 
