import csv

caminho_arquivo: str = 'exemplo.csv'

dados: list = []

with open(caminho_arquivo,mode = 'r', encoding = 'utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    
    for linha in leitor_csv:
        dados.append(linha)

for registro in dados:
    print(registro)