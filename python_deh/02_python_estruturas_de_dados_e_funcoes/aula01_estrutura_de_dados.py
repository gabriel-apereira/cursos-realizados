#Lista: coleção mutável e ordenada de elementos, que pode conter itens de tipos diferentes.

frutas = ['maçã', 'banana', 'laranja', 'uva']
print('Lista de frutas:', frutas)

# Acessar por indice
print('Primeira fruta:', frutas[0])
print('Segunda fruta:', frutas[1])

# Métodos comuns de listas
frutas.append('abacaxi')
print('Lista de frutas após adicionar abacaxi:', frutas)
frutas.insert(1, 'morango')
print('Lista de frutas após inserir morango na posição 1:', frutas)
frutas.remove('banana')
print('Lista de frutas após remover banana:', frutas)

print('Número de frutas na lista:', len(frutas))

#Tuplas: coleção ordenada e imutável de elementos, que pode conter itens de tipos diferentes.

coordenadas = (10, 20)
print('Coordenadas:', coordenadas)
print('X =', coordenadas[0])
print('Y =', coordenadas[1])

#Se tentar alterar da erro
# coordenadas[0] = 30  # Isso causará um erro, pois tuplas são imutáveis.

#Conjunto (set): coleção não ordenada e mutável de elementos únicos, sem elementos repetidos.
numeros = {1, 2, 3, 4, 5}
print('Conjunto de números:', numeros)

numeros.add(6)
numeros.add(3) #não será adicionado, pois já existe
print('Conjunto de números após adicionar 6 e tentar adicionar 3 novamente:', numeros)

pares = {2, 4, 6, 8}

print("União:", numeros.union(pares))
print("Interseção:", numeros.intersection(pares))
print("Diferença:", numeros.difference(pares))

#Dicionário: coleção mutável e ordenada de pares chave-valor, onde cada chave é única.

aluno = {
    'nome': 'João',
    'idade': 20,
    'curso': 'Engenharia'
}

print('Dicionário do aluno:', aluno)
print('Nome do aluno:', aluno['nome'])

#Adicionando/alterando chaves
aluno['idade'] = 21
aluno['cidade'] = 'São Paulo'
print('Dicionário do aluno após alterações:', aluno)

#Métodos uteis de dicionários
print('Chaves do dicionário:', aluno.keys())
print('Valores do dicionário:', aluno.values())
print('Itens do dicionário:', aluno.items())