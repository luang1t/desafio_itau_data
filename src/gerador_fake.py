from random import choice,uniform,choices,randint
from faker import Faker
import os
import pandas as pd

fake = Faker(locale='pt-BR') #REFERENCIANDO DE QUAL REGIÃO OS NOMES SERÃO RANDOMIZADOS

def criar_cliente(qtd_clientes = 1000): #FUNCAO PARA CRIAR CLIENTES
    
    lista_clientes = []

    print(f"Gerenado {qtd_clientes} clientes...")
    
    for _ in range(qtd_clientes): #ESTRUTURA DE REPETICAO CRIADA PARA CADASTRAR OS CLIENTES FICTICIOS
        
        operacoes = ['PIX','TED','DOC']
        categorias = ['MERCADO','LAZER','CONTAS']
        status = ['CONCLUIDA','FALHA','PENDENTE']
        pesos = [0.95 , 0.03 , 0.01]
        valor_transacao = uniform(100,10000) #RANDOMIZANDO O VALOR DA TRANSACAO ENTRE 100 E 10000 COM FLOAT
        
        cliente = {
        'nome': fake.name(), #CRIANDO NOMES ALEATORIOS BRASILEIROS
        'operacao':choice(operacoes), #ESCOLHENDO RANDOMICANTE AS OPCOES DA LISTA DE OPERACOES
        'valor' : valor_transacao,
        'categoria' : choice(categorias), #ESCOLHENDO RANDOMICANTE AS OPCOES DA LISTA DE OPERACOES
        'status':choices(status , weights=pesos, k=1)[0],
        }

        lista_clientes.append(cliente)

    return lista_clientes

'''
PARA SEGUIR UMA LINHA MAIS PROXIMA AO REAL, DECIDI COLOCAR PESOS(WEIGHTS) 
NO STATUS JA QUE NENHUM BANCO CONSEGUE SOBREVIVER SE 1 A CADA 3 TRANSACOES
FALHAREM. PARA ISSO SETEI UMA VARIAVEL(PESOS) CORRESPONDENTE A CADA TIPO DE STATUS.
O k DEFINE QUANTOS ELEMENTOS SERAO SORTEADOS OU SEJA, APENAS UM POR REQUISICAO.
ESSE [0] FOI UM POUCO ESTRANHO DE ENTENDER, CHOICES RETORNA UMA LISTA, UTLIZANDO [0]
O PYTHON 'PEGA' O VALOR DE DENTRO DA LISTA E ATRIBUI A VARIAVEL STATUS.
'''

if __name__ == "__main__":
    dados = criar_cliente(5000)
    df = pd.DataFrame(dados)

    os.makedirs('../data', exist_ok = True) #Cria uma pasta apenas se não existir uma com esse nome
    df.to_csv('../data/dados_bancarios.csv', index=False) #Converte o dataframe para csv e insere na pasta data/dados_bancarios.csv  index=false tira a numeração da tabela padrão
    print("CSV gerado com sucesso na pasta /data!")