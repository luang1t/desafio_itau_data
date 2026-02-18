import sqlite3
import pandas as pd
from pathlib import Path

#CONFIGURAÇÃO DE CAMINHOS

BASE_DIR = Path(__file__).parent.parent
CSV_PATH = BASE_DIR / 'data' / 'dados_bancarios.csv'
DB_PATH = BASE_DIR / 'data' / 'bradesco.db'

def carregar_dados_csv():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"Erro: Arquivo CSV não encontrado em {CSV_PATH}")
    
    print(f"Lendo dados de {CSV_PATH}")
    return pd.read_csv(CSV_PATH)

def salvar_no_banco(df):
    print(f"Conectando ao banco: {DB_PATH}")

    try:
        conn = sqlite3.connect(DB_PATH)

        df.to_sql('transacoes', conn, if_exists='replace', index=False)

        qtd = len(df)
        print(f"Sucesso! {qtd} registros inseridos na tabela 'transacoes'.")
    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    try:
        df_banco = carregar_dados_csv()
        salvar_no_banco(df_banco)
    except Exception as erro:
        print(f"Falha no processo ETL: {erro}")