

def ler_csv(caminho_arquivo: str) -> list[dict]:
    import csv
    dados = []
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linhas in leitor:
            dados.append(linhas)

    return dados


def filtrar_produtos_nao_entregues(dados: list[dict]) -> list[dict]:
    lista_produtos_filtrados = []
    for produto in dados:
        if produto.get("entregue") == 'False':
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados


def somar_valores_dos_produtos(dados: list[dict]) -> float:
    total = 0.0
    for produto in dados:
        total += float(produto.get("price"))
    return total

csv = ler_csv('python_jornada_de_dados/aula_07/desafio/vendas.csv')

produtos_n_entregues = filtrar_produtos_nao_entregues(csv)

total_valores = somar_valores_dos_produtos(produtos_n_entregues)

print(total_valores)


