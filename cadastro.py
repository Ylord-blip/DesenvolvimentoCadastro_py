#3. Objetivo Geral:
#Desenvolver uma solução em Python para o Coffee Shops Tia Rosa, que simule
#funcionalidades de um sistema de gerenciamento ou atendimento, como cadastro de produtos,
#pedidos, clientes, etc.
#3.1. Objetivos Específicos:
#I. Aplicar na prática os conceitos estudados na disciplina.
#II. Criar um sistema com interface simples (pode ser linha de comando).
#III. Demonstrar lógica de programação e uso de estruturas como listas, dicionários, funções, classes etc.
#IV. Produzir documentação explicativa do projeto.
#V. Compartilhar o código via GitHub, com acesso público.

from produtos import listar_produtos, escolher_produto, cadastrar_produtos
from clientes import cadastrar_cliente, listar_cliente
from pedidos import cadastrar_pedidos, listar_pedidos
    
    
# produtos_lista = ((nome_produto, valor_produto))
produtos_lista = [("Café Americano", 15), 
                  ("Cappuccino", 10), 
                  ("Latte", 8),
                  ('Notebook', 4500)]

# produtos_lista = (nome_cliente)
clientes_lista = ['Pedro',
                'Daniel',
                'Gabriel',
                ]

# pedidos_lista = [((nome_produto, valor_produto), nome_cliente)]
pedidos_lista = [(("Cappuccino", 10), 'Pedro')]

print('Olá, seja Bem-Vindo ao Coffee Shops da Tia Rosa')
print('Somo um ambiente acolhedor de café artesanal')

while(True):
    print('\n\nDigite a opção desejada: ')
    print('0 - Para sair do sistema')
    print('1 - Para listar produtos')
    print('2 - Para escolher produtos')
    print('3 - Para cadastrar produtos')
    print('4 - Para cadastrar clientes')
    print('5 - Para listar clientes')
    print('6 - Para listar pedidos')
    print('7 - Para cadastrar pedidos')



    opcao = int(input('Digite a escolha desejada: '))
    if opcao == 0:
        print('Saindo do sistema. Até mais...')
        break
    if opcao == 1:
        listar_produtos(produtos_lista)
    elif opcao == 2:
        escolher_produto(produtos_lista)
    elif opcao == 3:
        cadastrar_produtos(produtos_lista)
    elif opcao == 4:
        cadastrar_cliente(clientes_lista)
    elif opcao == 5:
        listar_cliente(clientes_lista)
    elif opcao == 6:
        listar_pedidos(pedidos_lista)
    elif opcao == 7:
        cadastrar_pedidos(pedidos_lista, clientes_lista, produtos_lista)

    












# opcao = int(input('Selecione a sua opção.\n0 - Americano.\n1 - Cappuccino.\n2 - Latte.\n'))

# bebida = opcoes_cafe[opcao]

# print(f'A bebida que você escolheu é {bebida[0]}, e o valor é R$ {bebida[1]}')



# # # print(opcao)
# # #input(opcao)
# # #print('Temos bebidas geladas também com várias opções', )
# # # opcao1 = ["Caramelo", "Baunilha", "Chocolate Belga"]
# # # input(opcao1)




