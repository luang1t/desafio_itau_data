from random import choice,uniform


def criar_cliente():
    operacoes = ['PIX','TED','DOC']
    valor_transacao = uniform(100,10000)
    categorias = ['MERCADO','LAZER','CONTAS']
    return {
        'operacao':choice(operacoes),
        'valor' : valor_transacao,
        'categoria' : choice(categorias)
    }

lista_clientes = []

numero_clientes = int(input("Digite o número de clientes que deseja cadastrar na lista: "))


for cadastro in range(numero_clientes):
    lista_clientes.append(criar_cliente())


for indice, cliente in enumerate (lista_clientes, start = 1):
        print(f'O {indice}º cliente escolheu {cliente["operacao"]} e transferiu R${cliente["valor"]:.2f} na categoria {cliente["categoria"]}.')