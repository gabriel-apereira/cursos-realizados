# 1 - Calcular Média de Valores em uma Lista
from typing import List

def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

# 2 - Filtrar Dados Acima de um Limite
def filtras_acima_de(valores: list[float], limite: float) -> list[float]:
    resultado = [ ]
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

# 3 - Contar Valores Únicos em uma Lista
def contar_valores_unicos(valores: List[float]) -> int:
    return len(set(valores))

# 4 - Converter Celsius para Fahrenheit em uma Lista
def converte_celcius_para_fahrenheit(celsius: List[float]) -> List[float]:
    return [(temp * 9/5) + 32 for temp in celsius]

# 5 - Calcular Desvio Padrão de uma Lista
def calcula_desvio_padrao(valores: list[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

# 6 - Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))
 