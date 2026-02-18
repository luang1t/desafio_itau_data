from random import choice,uniform,choices
from faker import Faker
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
CSV_PATH = DATA_DIR / 'dados_bancarios.csv'


fake = Faker(locale='pt-BR') #REFERENCIANDO DE QUAL REGIÃO OS NOMES SERÃO RANDOMIZADOS

def criar_cliente(qtd_clientes = 1000): #FUNCAO PARA CRIAR CLIENTES
    
    lista_clientes = []
    operacoes = ['PIX','TED','DOC']
    categorias = ['MERCADO','LAZER','CONTAS']
    status = ['CONCLUIDA','FALHA','PENDENTE']
    pesos = [0.95 , 0.01 , 0.03]
        

    print(f"Gerando {qtd_clientes} clientes...")
    
    for _ in range(qtd_clientes): #ESTRUTURA DE REPETICAO CRIADA PARA CADASTRAR OS CLIENTES FICTICIOS
        valor_transacao = uniform(100,10000) #RANDOMIZANDO O VALOR DA TRANSACAO ENTRE 100 E 10000 COM FLOAT

        cliente = {
        'nome': fake.name(), #CRIANDO NOMES ALEATORIOS BRASILEIROS
        'operacao':choice(operacoes), #ESCOLHENDO RANDOMICANTE AS OPCOES DA LISTA DE OPERACOES
        'valor' : valor_transacao,
        'categoria' : choice(categorias), #ESCOLHENDO RANDOMICANTE AS OPCOES DA LISTA DE OPERACOES
        'status':choices(status , weights=pesos, k=1)[0]
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

def gerar_dados_csv(qtd=5000):
    dados = criar_cliente(qtd)
    df = pd.DataFrame(dados)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(CSV_PATH, index=False)
    print(f"CSV gerado com sucesso em: {CSV_PATH}")



if __name__ == "__main__":
    gerar_dados_csv()