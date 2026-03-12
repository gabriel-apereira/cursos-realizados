# Desafio
# Peça a idade de várias pessoas e conte:
# - quantos tem menos de 18 anos
# - quantos tem entre 18 ou mais
# O programa deve parar quando digitar idade negativa

contador_menor_18 = 0
contador_18_ou_mais = 0

for i in range(100):  # Loop para permitir várias entradas, pode ser ajustado conforme necessário
    idade = int(input("Digite a idade (ou um número negativo para encerrar): "))
    
    if idade < 0:
        print("Encerrando o programa.")
        break
    elif idade < 18:
        contador_menor_18 += 1
    else:
        contador_18_ou_mais += 1

print(f"\nQuantidade de pessoas com menos de 18 anos: {contador_menor_18}")
print(f"Quantidade de pessoas com 18 anos ou mais: {contador_18_ou_mais}")