# 1) Solicita ao usuário que digite seu nome

nome = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))

# 4) Calcule o valor do bônus final
bonus_final = salario * (bonus / 100)

# 5) Imprima cálculo do KPI para o usuário
kpi = 1000 + salario + bonus_final

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome}, seu salário é {salario} e seu bônus final é {bonus_final}. Seu KPI é {kpi}.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?