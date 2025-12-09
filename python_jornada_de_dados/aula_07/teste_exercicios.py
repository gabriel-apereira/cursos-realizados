def filtrar_acima_de(valores: list[float], limite: float) -> list[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado


print(filtrar_acima_de([1, 5, 8, 10, 3], 5))
