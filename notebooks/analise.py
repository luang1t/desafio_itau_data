import sqlite3
import pandas as pd
import matplotlib.pyplot as plt  

conn = sqlite3.connect('bradesco.db')

#TOTAL DE DINHEIRO MOVIMENTADO
query01 = "SELECT SUM(valor) as Total_Movimentado FROM transacoes " #SELECIONANDO E SOMANDO O TOTAL MOVIMENTADO NA TABELA
df_total = pd.read_sql(query01,conn)

#QUANTAS FALHAS TIVEMOS
query02 = "SELECT COUNT(*) as Qtd_Falhas FROM transacoes WHERE status = 'FALHA' " #SELECIONANDO E CONTANDO OS NUMEROS DE FALHAS
df_falhas = pd.read_sql(query02,conn)

#TOTAL OPERACAO POR PIX
query03 = "SELECT SUM(valor) as Qtd_PIX FROM transacoes WHERE operacao = 'PIX' "
df_pix_operacao = pd.read_sql(query03,conn)

#RANKING DAS OPERAÇÕES
query04 = "SELECT operacao, SUM(valor) as cada_operacao_total FROM transacoes GROUP BY operacao ORDER BY cada_operacao_total DESC"
df_total_operacoes = pd.read_sql(query04,conn)

#RANKING DAS CATEGORIAS
query05 = "SELECT categoria, SUM(valor) as maior_por_categoria FROM transacoes GROUP BY categoria ORDER BY maior_por_categoria DESC"
df_maior_por_categoria = pd.read_sql(query05,conn)

#RANKING DAS OPERAÇÕES DENTRO DA CATEGORIA LAZER
query06 = "SELECT categoria, operacao, SUM(valor) as lazer_oper_mais_realizadas FROM transacoes WHERE categoria = 'LAZER' GROUP BY operacao ORDER BY lazer_oper_mais_realizadas DESC"
df_lazer_oper_mais_realizadas = pd.read_sql(query06,conn)

#
query07 = "SELECT valor FROM transacoes"
df_todas = pd.read_sql(query07, conn)

print('--- Resultado da pesquisa ---')
print(f'Total de dinheiro movimentado:\nR$:{df_total['Total_Movimentado'][0]:,.2f}')#AQUI USAMOS O [0] PARA REFERENCIAR O INDICE DA TABELA QUE QUEREMOS

'''
Total_Movimentado
0    |  489239.31
'''
print(f'Total de falhas na operação: {df_falhas['Qtd_Falhas'][0]}')#AQUI USAMOS O [0] PARA REFERENCIAR O INDICE DA TABELA QUE QUEREMOS

'''
Qtd_Falhas
0    |  2
'''

print(f'Operações PIX:\nR$:{df_pix_operacao['Qtd_PIX'][0]:,.2f}')

print("Ranking das OPERAÇÕES")
for index, linha in df_total_operacoes.iterrows():
    print(f"{index+1}º Lugar: {linha['operacao']} R$:{linha['cada_operacao_total']:,.2f}")

print("-*-"*20)
print("Ranking das CATEGORIAS")
for index, linha in df_maior_por_categoria.iterrows():
    print(f"{index+1}º Lugar {linha['categoria']} R$:{linha['maior_por_categoria']:,.2f}")

print("-*-"*20)
print("Ranking das OPERAÇÕES em CATEGORIAS")
for index,linha in df_lazer_oper_mais_realizadas.iterrows():
    print(f"{index+1}º Lugar {linha['operacao']} R$:{linha['lazer_oper_mais_realizadas']:,.2f}")

#---------------------------------------------------------------------------------------------------
operacoes = df_total_operacoes['operacao']
valores = df_total_operacoes['cada_operacao_total']
valores_categorias = df_maior_por_categoria['maior_por_categoria']
rankin_operacao_lazer = df_lazer_oper_mais_realizadas['lazer_oper_mais_realizadas']

plt.figure(1,figsize=(8, 5))
plt.bar(operacoes,valores,color=['#cc0000','#00ff00','#0000ff'])
plt.title("Volume Financeiro por Operação")
plt.ylabel("Valor Total (R$)")
plt.xlabel("Tipo de Operação")
plt.show()

plt.figure(2)
plt.hist(df_todas['valor'], bins=10, color='green', edgecolor='black')
plt.title('Distribuição dos valores (Histograma)')
plt.xlabel('Faixas de Valor (R$)')
plt.ylabel('Quantidade de Transações')
plt.show()

conn.close()
