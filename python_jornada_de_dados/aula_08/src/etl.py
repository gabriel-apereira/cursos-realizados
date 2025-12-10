import pandas as pd
import os
import glob

# função de extract que le e consolida os json


def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# uma função que transforma
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

# carregar dados em csv ou parquet ou nos 2
def carregar_dados(df: pd.DataFrame, caminho_saida: str, formato: list) -> None:
    if 'parquet' in formato:
        df.to_parquet(caminho_saida + '.parquet', index=False)
    if 'csv' in formato:
        df.to_csv(caminho_saida + '.csv', index=False)
    return None

#função de pipeline rodando tudo
def pipeline_calculo_kpi(pasta: str, caminho_saida: str, formato: list) -> pd.DataFrame:
    df = extrair_dados(pasta)
    df = calcular_kpi_total_vendas(df)
    carregar_dados(df, caminho_saida, formato)
    return df, print(f"Dados salvos em {caminho_saida} nos formatos: {formato}")