# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1 = int(input("Digite o primeiro número inteiro:"))
num2 = int(input("Digite o segundo número inteiro:"))
soma = num1 + num2
print("A soma dos números é:", soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um número inteiro:"))
resto = num % 5
print("O resto da divisão do número por 5 é:", resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num3 = int(input("Digite o primeiro número inteiro:"))
num4 = int(input("Digite o segundo número inteiro:"))
produto = num3 * num4
print("O produto dos números é:", produto)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num5 = int(input("Digite o primeiro número inteiro:"))
num6 = int(input("Digite o segundo número inteiro:"))
divisao_inteira = num5 // num6
print("A divisão inteira do primeiro número pelo segundo é:", divisao_inteira)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num7 = int(input("Digite um número inteiro:"))
quadrado = num7 ** 2
print("O quadrado do número é:", quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
flt1 = float(input("Digite o primeiro número flutuante:"))
flt2 = float(input("Digite o segundo número flutuante:"))
soma_flt = flt1 + flt2
print("A soma dos números flutuantes é:", soma_flt)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
flt3 = float(input("Digite o primeiro número flutuante:"))
flt4 = float(input("Digite o segundo número flutuante:"))
media = (flt3 + flt4) / 2
print("A média dos números flutuantes é:", media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base (número flutuante):"))
expoente = float(input("Digite o expoente (número flutuante):"))
potencia = base ** expoente
print("O resultado da potência é:", potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em Fahrenheit é:", fahrenheit)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo:"))
area = 3.14159 * (raio ** 2)
print("A área do círculo é:", area)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite uma string:")
texto_maiusculas = texto.upper()
print("A string em maiúsculas é:", texto_maiusculas)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo:")
nome_minusculas = nome_completo.lower()
print("Seu nome em minúsculas é:", nome_minusculas)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase:")
frase_sem_espacos = frase.strip()
print("A frase sem espaços em branco no início e no final é:", frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)  
print("Mês:", mes)
print("Ano:", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
str1 = input("Digite a primeira string:")
str2 = input("Digite a segunda string:")
concatenacao = str1 + str2
print("A concatenação das strings é:", concatenacao)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
data1 = input("Digite a primeira expressão booleana (True/False): ").strip().lower()
data2 = input("Digite a segunda expressão booleana (True/False): ").strip().lower()
expr1 = (data1 == "true")
expr2 = (data2 == "true")
resultado_and = expr1 and expr2
print("O resultado da operação AND é:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
data3 = input("Digite a primeira expressão booleana (True/False): ").strip().lower()
data4 = input("Digite a segunda expressão booleana (True/False): ").strip.lower()
expr3 = (data3 == "true")
expr4 = (data4 == "true")
resultado_or = expr3 or expr4
print("O resultado da operação OR é:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
data5 = input("Digite uma expressão booleana (True/False): ").strip().lower()
expr5 = (data5 == "true")
resultado_not = not expr5
print("O valor invertido é:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num8 = float(input("Digite o primeiro número:"))
num9 = float(input("Digite o segundo número:"))
iguais = (num8 == num9)
print("Os números são iguais?", iguais)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num10 = float(input("Digite o primeiro número:"))
num11 = float(input("Digite o segundo número:"))
diferentes  = (num10 != num11)
print("Os números são iguais?", diferentes)

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius_input = float(input("Digite a temperatura em Celsius: "))
    fahrenheit_output = (celsius_input * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit_output}")
except ValueError:
    print("Entrada inválida! Por favor, insira um número válido para a temperatura.")

# 22: Verificador de Palíndromo
try:
    palavra = input("Digite uma palavra: ").strip()
    if palavra == palavra[::-1]:
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")
except Exception as e:
    print("Ocorreu um erro:", e)

# 23: Calculadora Simples
try:
    num_a = float(input("Digite o primeiro número: "))
    num_b = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ").strip()

    if operacao == "+":
        resultado = num_a + num_b
    elif operacao == "-":
        resultado = num_a - num_b
    elif operacao == "*":
        resultado = num_a * num_b
    elif operacao == "/":
        if num_b != 0:
            resultado = num_a / num_b
        else:
            print("Erro: Divisão por zero não é permitida.")
            resultado = None
    else:
        print("Operação inválida!")
        resultado = None

    if resultado is not None:
        print(f"O resultado de {num_a} {operacao} {num_b} é: {resultado}")
except ValueError:
    print("Entrada inválida! Por favor, insira números válidos.")

# 24: Classificador de Números
try:
    numero = float(input("Digite um número: "))
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")
except ValueError:
    print("Entrada inválida! Por favor, insira um número válido.")

# 25: Conversão de Tipo com Validação
try:
    entrada = input("Digite um valor numérico: ")
    numero_convertido = float(entrada)
    print(f"O valor convertido é: {numero_convertido}")
except ValueError:
    print("Entrada inválida! Por favor, insira um número válido.")
