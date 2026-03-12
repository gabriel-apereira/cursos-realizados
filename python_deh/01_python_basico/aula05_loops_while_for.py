contador = 1

print("Contador usando while:")
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1


senha_correta = 'python123'
tentativa = input("\nDigite a senha: ")

while tentativa != senha_correta:
    print("Senha incorreta. Tente novamente.")
    tentativa = input("Digite a senha: ")

print("Acesso concedido.")

print("\nPercorrendo lista usando for:")
frutas = ['maçã', 'banana', 'laranja', 'uva']
for fruta in frutas:
    print(f"Fruta: {fruta}")

print("\nContando de 1 a 10 usando for:")
for i in range(1, 11):
    print(f"Número: {i}")

print("\nexemplo de break e continue:")
for i in range(1, 11):
    if i == 5:
        print("Número 5 encontrado, interrompendo o loop.")
        break

for i in range(1, 11):
    if i % 2 == 0:
        print(f"Número {i} é par, pulando para o próximo.")
        continue
    print(f"Número {i} é ímpar.")