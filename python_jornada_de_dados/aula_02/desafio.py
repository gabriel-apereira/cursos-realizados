### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")
    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
        exit()
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
        exit()
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        raise ValueError("O salário não pode ser negativo.")
        exit()
    else:
        print("Salário válido:", salario)
except ValueError as e:
    print(e)
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus = float(input("Digite o valor do bônus recebido (em %): "))
    if bonus < 0:
        raise ValueError("O bônus não pode ser negativo.")
        exit()
    else:
        print("Bônus válido:", bonus)
except ValueError as e:
    print(e)
    exit()

# 4) Calcule o valor do bônus final
valor_bonus = (bonus / 100) * salario + 1000

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá, {nome}! Seu salário é R${salario:.2f} e o valor do bônus final é R${valor_bonus:.2f}.")