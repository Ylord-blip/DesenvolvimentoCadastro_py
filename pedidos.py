
def cadastrar_pedidos(pedidos_lista, clientes_lista, produtos_lista):
    nome_cliente = input('Informe o nome do cliente: ')
    nome = None
    for cliente in enumerate(clientes_lista):
        # print(cliente[1])
        if cliente[1] == nome_cliente:
            nome = cliente[1]
            break

    if nome is None:
        print('Cliente não cadastrado')
        return
    
    nome_produto = input('Informe o nome do produto: ')
    produto_cliente = None
    produto_cadastro = None
    for produto in enumerate(produtos_lista):
        if produto[1][0] == nome_produto:
           produto_cliente = produto[1][0]
           produto_cadastro = produto[1]
           break

    if produto_cliente is None:
        print('Produto não cadastrado')
        return
        
    print(f'Cliente {nome}')
    print(f'Produto {produto_cadastro}')


    pedidos_lista.append((produto_cadastro, nome))


def listar_pedidos(pedidos_lista):
    print('Temos os seguintos pedidos disponíveis: ')

    for pedido in enumerate(pedidos_lista):
        print(pedido)


    