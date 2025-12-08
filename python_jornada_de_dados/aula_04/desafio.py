### Desafio - Transformar o códigod a ultima aula em função, e salvar toda vez que rodar em um dicionario
import json

def cadastro_bonus():
    nome_valido = False
    salario_valido = False
    bonus_valido = False

    # 1) Solicita ao usuário que digite seu nome
    while not nome_valido:
        try:
            nome = input("Digite seu nome: ")
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                print("Nome válido:", nome)
                nome_valido = True
        except ValueError as e:
            print(e)

    # 2) Solicita o salário
    while not salario_valido:
        try:
            salario = float(input("Digite seu salário: "))
            if salario < 0:
                raise ValueError("O salário não pode ser negativo.")
            else:
                print("Salário válido:", salario)
                salario_valido = True
        except ValueError as e:
            print(e)

    # 3) Solicita o bônus
    while not bonus_valido:
        try:
            bonus = float(input("Digite o valor do bônus recebido (em %): "))
            if bonus < 0:
                raise ValueError("O bônus não pode ser negativo.")
            else:
                print("Bônus válido:", bonus)
                bonus_valido = True
        except ValueError as e:
            print(e)

    # 4) Calcula o valor do bônus final
    valor_bonus = (bonus / 100) * salario + 1000

    # 5) Mensagem personalizada
    print(f"Olá, {nome}! Seu salário é R${salario:.2f} "
          f"e o valor do bônus final é R${valor_bonus:.2f}.")

    # Retorna os dados em um dicionário
    return {
        "nome": nome,
        "salario": salario,
        "bonus": bonus,
        "valor_bonus": valor_bonus
    }

#Salva o dicionario em JSON
dados = cadastro_bonus()

with open("cadastros.json","a", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)
    arquivo.write("\n")

print("Dados salvos com sucesso em 'cadastros.json'.")
