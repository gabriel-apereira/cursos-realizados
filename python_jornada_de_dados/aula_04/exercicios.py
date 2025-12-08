#1 - Lista de números ao quadrado
numeros: list = [range(1,11)]
quadrado = [n**2 for n in numeros[0]]
print(quadrado)

#2 - Modificar lista de linguagens
linguagens = ["Python", "Java", "C++", "JavaScript"] 
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

#3 - Informações de 1 livro
livro: dict = {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

#4 - Contar ocorrências de caracteres
def contar_caracteres(string):
    contagem = {}
    for caractere in string:
        contagem[caractere] = contagem.get(caractere,0) + 1
    return contagem

print(contar_caracteres("banana"))

#5 - Preço total da lista de compras
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: R$ {total:.2f}")

#6 - Eliminação de duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
lista_unicos = list(set(emails))
print(lista_unicos)

#7 - Filtragem de dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]
print(idades_validas)

#8 - Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)

#9 - Agregação de Dados
#Objetivo: Dado um conjunto de números, calcular a média.
numeros = [10, 20, 30, 40, 50]

medias = sum(numeros) / len(numeros)
print(f"Média: {medias}")

# 10 - Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [v for v in valores if v % 2 == 0]
impares = [v for v in valores if v % 2 != 0]
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

# 11 - Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

for produto in produtos:
    if produto["id"] == 1:
        produto["preço"] = 90

print(produtos)

# 12 - Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}
print(dicionario_fundido)

#13 - Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
estoque_filtrado = {produto: quantidade for produto,quantidade in estoque.items() if quantidade >0}
print(estoque_filtrado)

#14 - Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dados = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
chaves = list(dados.keys())
valores = list(dados.values())

print(f"Chaves: {chaves}")
print(f"Valores: {valores}")

#15 -Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    frequencia[caractere] = frequencia.get(caractere,0) + 1

print(frequencia)

#16 - Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def soma_numeros(lista: list) -> int:
    return sum(lista)

#17 - Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def eh_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

#18 - Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def revert_string(string: str) -> str:
    return string[::-1]

#19 - Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def encontrar_pares(lista: list, alvo: int) -> list:
    pares = []
    vistos = set()
    
    for numero in lista:
        complemento = alvo - numero
        if complemento in vistos:
            pares.append((complemento, numero))
        vistos.add(numero)
    
    return pares

#20 - Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
def chave_ordenadas(dicionario: dict) -> list:
    return sorted(dicionario.keys())