import sqlite3
import pandas as pd
import matplotlib.pyplot as plt  


def conectar_banco():
    return sqlite3.connect('./data/bradesco.db')

def imprimir_ranking(titulo, dataframe, col_nome, col_valor):
    print(f"\n--- {titulo} ---")
    for idx, row in dataframe.iterrows():
        print(f"{idx+1}º | {row[col_nome]:<15} | R$ {row[col_valor]:,.2f}")



def main():
    conn = conectar_banco()

    #Extração de dados(ETL)
    df_total = pd.read_sql("SELECT SUM(valor) as Total_Movimentado FROM transacoes", conn)
    df_falha = pd.read_sql("SELECT COUNT(*) as Qtd_Falhas FROM transacoes WHERE status = 'FALHA'", conn)

    df_ranking_operacoes = pd.read_sql("""
                            SELECT operacao, SUM(valor) as ranking_operacoes 
                            FROM transacoes 
                            GROUP BY operacao ORDER BY ranking_operacoes DESC
                        """, conn)  
      
    df_rankin_oper_lazer = pd.read_sql("""
                            SELECT operacao, SUM(valor) as ranking_oper_lazer 
                            FROM transacoes WHERE categoria = 'LAZER' 
                            GROUP BY operacao ORDER BY ranking_oper_lazer DESC
                        """, conn)
    
    print("RELATÓRIO TERMINAL")
    print(F"Total Movimentado: R$ {df_total.iloc[0,0]:,.2f}") #Usei .iloc[0,0] para especificar que quero o elemento da linha 0 coluna 0
    print(f"Total de Falhas: {df_falha.iloc[0,0]}")

    imprimir_ranking("Ranking Geral", df_ranking_operacoes, "operacao", "ranking_operacoes")
    imprimir_ranking("Ranking Operações em Lazer",df_rankin_oper_lazer,"operacao", "ranking_oper_lazer")

    fig,(ax1,ax2) = plt.subplots(1,2, figsize=(12,5))
    
    ax1.bar(df_ranking_operacoes['operacao'],df_ranking_operacoes['ranking_operacoes'], color = ['#cc0000', '#333333', '#999999'])
    ax1.set_title("Volume por Operação")

    ax2.pie(df_ranking_operacoes['ranking_operacoes'], labels=df_ranking_operacoes['operacao'], autopct='%1.1f%%')
    ax2.set_title("Share de Mercado")

    plt.tight_layout()
    plt.show()

    conn.close()

if __name__ == "__main__":
    main()