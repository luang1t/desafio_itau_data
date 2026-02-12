from random import choice,uniform
from faker import Faker
import pandas as pd

fake = Faker(locale='pt-BR') #REFERENCIANDO DE QUAL REGIÃO OS NOMES SERÃO RANDOMIZADOS

def criar_cliente(): #FUNCAO PARA CRIAR CLIENTES

    operacoes = ['PIX','TED','DOC']
    categorias = ['MERCADO','LAZER','CONTAS']
    status = ['CONCLUIDA','FALHA','PENDENTE']
    valor_transacao = uniform(100,10000) #RANDOMIZANDO O VALOR DA TRANSACAO ENTRE 100 E 10000 COM FLOAT

    return {
        'operacao':choice(operacoes), #ESCOLHENDO RANDOMICANTE AS OPCOES DA LISTA DE OPERACOES
        'categoria' : choice(categorias), #ESCOLHENDO RANDOMICANTE AS OPCOES DA LISTA DE OPERACOES
        'status':choice(status), #ESCOLHENDO RANDOMICAMENTE AS OPCOES DA LISTA DE STATUS
        'valor' : valor_transacao,
        'nome': fake.name() #CRIANDO NOMES ALEATORIOS BRASILEIROS
    }

lista_clientes = []

numero_clientes = int(input("Digite o número de clientes que deseja cadastrar na lista: "))


for cadastro in range(numero_clientes): #ESTRUTURA DE REPETICAO CRIADA PARA CADASTRAR OS CLIENTES FICTICIOS
    lista_clientes.append(criar_cliente())


for indice, cliente in enumerate (lista_clientes, start = 1):
        print(f'{indice}º: O {cliente["nome"]} escolheu {cliente["operacao"]} e transferiu R${cliente["valor"]:.2f} na categoria {cliente["categoria"]}. {cliente["status"]}')

print("Gerando arquivo CSV...")

df = pd.DataFrame(lista_clientes) #DEFININDO MEU DATAFRAME UTLIZANDO PANDAS E A LISTA CRIADA

df.to_csv('dados_bancarios.csv', index = False) #CONVERTENDO MEU DATAFRAME EM CSV

print("Arquivo 'dados_bancarios.csv' criado com sucesso!")