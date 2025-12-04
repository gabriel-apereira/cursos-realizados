### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
nome_valido = False
salario_valido = False
bonus_valido = False

# 1) Solicita ao usuário que digite seu nome
while nome_valido is not True:
    try:
        nome = input("Digite seu nome: ")
        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
while salario_valido is not True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        else:
            print("Salário válido:", salario)
            salario_valido = True
    except ValueError as e:
        print(e)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
while bonus_valido is not True:
    try:
        bonus = float(input("Digite o valor do bônus recebido (em %): "))
        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
        else:
            print("Bônus válido:", bonus)
            bonus_valido = True
    except ValueError as e:
        print(e)

# 4) Calcule o valor do bônus final
valor_bonus = (bonus / 100) * salario + 1000

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá, {nome}! Seu salário é R${salario:.2f} e o valor do bônus final é R${valor_bonus:.2f}.")