from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta_argumento: str = 'data'
output: list = ['parquet']

pipeline_calcular_kpi_de_vendas_consolidado(pasta_argumento, output)