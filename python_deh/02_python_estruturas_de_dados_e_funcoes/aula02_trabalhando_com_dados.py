# Iterando listas
numeros = [10, 5, 3, 8, 2]

print('Números originais:', numeros)
for n in numeros:
    print(n)

# Filtros e buscas simples em listas
maior_que_7 = []
for n in numeros:
    if n > 7:
        maior_que_7.append(n)
print('Números maiores que 7:', maior_que_7)

#Buscar se um valor está na lista
busca = 9
if busca in numeros:
    print(f'O número {busca} está na lista.')
else:
    print(f'O número {busca} não está na lista.')

# Iterando dicionários
aluno = {
    'nome': 'Maria',
    'idade': 22,
    'curso': 'Medicina'
}

for chave in aluno:
    print(f'{chave}: {aluno[chave]}')

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')

# Ordenação e transformação de dados
ordenada_crescente = sorted(numeros)
print('Números ordenados em ordem crescente:', ordenada_crescente)
ordenada_decrescente = sorted(numeros, reverse=True)
print('Números ordenados em ordem decrescente:', ordenada_decrescente)

for n in numeros:
    print(f'O quadrado de {n} é {n**2}')

quadrados = []
for n in numeros:
    quadrados.append(n**2)
print('Lista de quadrados:', quadrados)