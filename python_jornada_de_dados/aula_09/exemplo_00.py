from loguru import logger

# print -> logger.info

logger.add("meu_log.log", level = 'CRITICAL')

def soma(x,y):
    try:
        soma = x+y
        logger.info(f"Soma realizada com sucesso: {soma}")
        return soma
    except Exception as e:
        logger.critical(f"Variaveis nao sao numeros")

soma(2,"3")