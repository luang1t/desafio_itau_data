import sqlite3
import pandas as pd


conn = sqlite3.connect('bradesco.db') #Conecta o banco, cria o arquivo .db dentro da pasta notebooks

df = pd.read_csv('./dados_bancarios.csv') #Criando o meu dataframe pegando os dados ja criados em csv do arquivo em questao

df.to_sql('transacoes', conn, if_exists='replace', index=False) #One-Liner o coração do ETL(Extract, Transform, Load)

'''
'transacoes'        - significa o nome que estou dando a minha tabela
conn                - diz em qual banco eu vou adicionar meus dados
if_exists='replace' - significa que se ja existir uma tabela ele tem quem exluir e usar a nova fazendo um DROP TABLE
index=false         - significa que estou dizendo ao banco de dados ignorar a numerçao de linhas do python
'''

conn.close()