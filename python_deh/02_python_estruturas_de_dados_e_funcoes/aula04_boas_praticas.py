# Escopo de variaveis
msg_global = 'Essa é uma variável global'

def exemplo_escopo():
    msg_local = 'Essa é uma variável local'
    print(msg_global)  # Variável global pode ser acessada dentro da função
    print(msg_local)   # Variável local pode ser acessada dentro da função

exemplo_escopo()
# print(msg_local)  # Isso causará um erro, pois msg_local não é acessível fora da função

# Funções pequenas e reutilizáveis
def calcular_desconto(preco, percentual):
    return preco * (1 - percentual / 100)

preco_original = 100
desconto = 20
preco_com_desconto = calcular_desconto(preco_original, desconto)
print(f'Preço original: {preco_original}, Desconto: {desconto}%, Preço com desconto: {preco_com_desconto}')

# Nomeação clara e organização de código
# Boas praticas de nomeação: 
# usar nomes descritivos para variáveis e funções, evitar abreviações confusas,
# e seguir convenções de estilo (como snake_case para funções e variáveis).

def somar_lista(numeros):
    """Retorna a soma de uma lista de números."""
    return sum(numeros)

numeros = [1, 2, 3, 4, 5]
resultado = somar_lista(numeros)
print(f'A soma dos números é: {resultado}')