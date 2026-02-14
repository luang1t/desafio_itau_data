import sqlite3
import pandas as pd

conn = sqlite3.connect('bradesco.db')

#TOTAL DE DINHEIRO MOVIMENTADO
query01 = "SELECT SUM(valor) as Total_Movimentado FROM transacoes" #SELECIONANDO E SOMANDO O TOTAL MOVIMENTADO NA TABELA
df_total = pd.read_sql(query01,conn)

#QUANTAS FALHAS TIVEMOS
query02 = "SELECT COUNT(*) as Qtd_Falhas FROM transacoes WHERE status = 'FALHA' " #SELECIONANDO E CONTANDO OS NUMEROS DE FALHAS
df_falhas = pd.read_sql(query02,conn)

print('--- Resultado da pesquisa ---')
print(f'Total de dinheiro movimentado: R${df_total['Total_Movimentado'][0]:,.2f}')#AQUI USAMOS O [0] PARA REFERENCIAR O INDICE DA TABELA QUE QUEREMOS

'''
Total_Movimentado
0    |  489239.31
'''
print(f'Total de falhas na operação: {df_falhas['Qtd_Falhas'][0]}')#AQUI USAMOS O [0] PARA REFERENCIAR O INDICE DA TABELA QUE QUEREMOS

'''
Qtd_Falhas
0    |  2
'''

conn.close()