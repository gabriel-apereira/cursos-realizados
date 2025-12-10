from etl import pipeline_calculo_kpi

pasta_argumento: str = 'python_jornada_de_dados\\aula_08\\data'
caminho_saida_argumento: str = 'python_jornada_de_dados\\aula_08\\output\\dados'
formato_argumento: list = ['parquet', 'csv']

df = pipeline_calculo_kpi(pasta_argumento,caminho_saida_argumento, formato_argumento)
print(df)