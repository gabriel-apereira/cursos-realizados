# Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
# Elas ajudam a organizar o código, melhorar a legibilidade e evitar repetição.

# Criando funções com def
def dizer_ola():
    print('Olá!')


dizer_ola()  # Chamando a função


def saudacao(nome):
    print(f'Olá, {nome}!')


saudacao('Alice')  # Chamando a função com argumento

# Parametros e retorno


def soma(a, b):
    return a + b


resultado = soma(5, 3)
print(f'O resultado da soma é: {resultado}')


def media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)


notas = [7, 8, 9]
print(f'A média das notas é: {media(notas)}')

def apresentar_pessoa(nome, idade = 18, cidade = 'Não informada'):
    print(f'Meu nome é {nome}, tenho {idade} anos e moro em {cidade}.')

apresentar_pessoa('Carlos')  # Usando valores padrão
apresentar_pessoa('Ana', 25)  # Sobrescrevendo o valor padrão de idade
apresentar_pessoa('Beatriz', 30, cidade='Rio de Janeiro')  # Sobrescrevendo o valor padrão de cidade
