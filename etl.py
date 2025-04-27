import pandas as pd
import os
import glob
from utils_log import log_decorator

# uma funcao de extract que le e consolida os json

@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# uma funcao que trasforma
@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df
# uma funcao que faz load em csv ou parquet
@log_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    for formato in format_saida:    
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)

# uma funcao que roda o pipeline todo
@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(dir: str, output: list):
    data_frame = extrair_dados_e_consolidar(dir)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, output)             
