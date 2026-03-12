nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}! Você tem {idade} anos.")

# Operadores de comparação
# == igual
# != diferente
# > maior que 
# < menor que
# >= maior ou igual a
# <= menor ou igual a

maior_de_idade = idade >= 18
print(f"Você é maior de idade? {maior_de_idade}")

if idade < 12:
    categoria = 'criança'
elif idade < 18:
    categoria = 'adolescente'
elif idade < 60:
    categoria = 'adulto'
else:
    categoria = 'idoso'

print(f"Você é {categoria}.")