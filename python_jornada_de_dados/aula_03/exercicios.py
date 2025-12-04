### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
try:
    quantidade = int(input("Digite a quantidade vendida: "))
    preco = float(input("Digite o preço do produto: "))

    if quantidade > 0 and preco > 0:
        print("Dados válidos")
    else:
        print("Dados inválidos")
except ValueError:
    print("Entrada inválida. Por favor, insira números válidos.")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
try:
    temperatura = float(input("Digite a leitura de temperatura: "))

    if temperatura < 18:
        print("Baixa")
    elif 18 <= temperatura <= 25:
        print("Normal")
    else:
        print("Alta")
except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])
else:
    print("Nenhum erro encontrado.")

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
usuario = {'nome': 'Gabriel', 'idade': 30, 'email': 'gabriel@example.com'}
if 18 <= usuario['idade'] <= 65:
    if "@" in usuario['email'] and ".com" in usuario['email']:
        print("Dados de usuário válidos")
    else:
        print("Email inválido")
else:
    print("Idade inválida")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita")
else:
    print("Transação normal")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = 'hoje e nossa segunda aula do bootcamp , bootcamp de python'

contragem_de_palavras = {}
palavras = texto.split()

for palavra in palavras:
    if palavra in contragem_de_palavras:
        contragem_de_palavras[palavra] += 1
    else:
        contragem_de_palavras[palavra] = 1
print(contragem_de_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [10, 20, 30, 40, 50]
min_num = min(numeros)
max_num = max(numeros)
numeros_normalizados = [(num - min_num) / (max_num - min_num) for num in numeros]
print(numeros_normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
usuarios = [
    {'nome': 'Alice', 'idade': 28}, 
    {'nome': 'Bob'}, 
    {'nome': 'Charlie', 'idade': 35}]
usuarios_com_idade = [usuario for usuario in usuarios if 'idade' in usuario]
print(usuarios_com_idade)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in numeros if num % 2 ==0]
print(numeros_pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {'categoria': 'Eletrônicos', 'valor': 1500},
    {'categoria': 'Roupas', 'valor': 500},
    {'categoria': 'Eletrônicos', 'valor': 700},
    {'categoria': 'Alimentos', 'valor': 300},
    {'categoria': 'Roupas', 'valor': 200}
]
agregado_vendas = {}
for venda in vendas:
    categoria = venda['categoria']
    valor = venda['valor']
    if categoria in agregado_vendas:
        agregado_vendas[categoria] += valor
    else:
        agregado_vendas[categoria] = valor
print(agregado_vendas)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
while True:
    entrada = input("Digite um dado (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        print("Encerrando a leitura de dados.")
        break
    else:
        print(f"Dado recebido: {entrada}")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
while True:
    try:
        numero = int(input("Digite um número entre 1 e 10: "))
        if 1 <= numero <= 10:
            print(f"Número válido: {numero}")
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
api = {
    'pagina_1': ['dado1', 'dado2'],
    'pagina_2': ['dado3', 'dado4'],
    'pagina_3': []
}
while True:
    pagina_atual = f'pagina_{len(api) - len([p for p in api.values() if not p]) + 1}'
    dados = api.get(pagina_atual, [])
    if not dados:
        print("Nenhum dado restante para processar.")
        break
    for dado in dados:
        print(f"Processando {dado}")
    api[pagina_atual] = []  # Simula que a página foi processada

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
serviço_disponivel = False
tentativas = 0

while tentativas < 5:
    tentativas += 1
    print(f"Tentativa {tentativas} de conexão...")
    if serviço_disponivel:
        print("Conexão bem-sucedida!")
        break
    else:
        print("Falha na conexão. Tentando novamente...")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
itens = [1, 2, 3, 4, 'parar', 5, 6]
for item in itens:
    if item == 'parar':
        print("Condição de parada encontrada. Encerrando o processamento.")
        break
    print(f"Processando item: {item}")