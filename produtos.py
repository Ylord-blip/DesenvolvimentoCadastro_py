
def listar_produtos(produtos_lista):
    print('Temos os seguintos produtos disponíveis: ')

    for indice, produto in enumerate(produtos_lista):
        print(f'O produto {produto[0]} custa R$ {produto[1]}')



def escolher_produto(produtos_lista):
    escolha = input('Favor informar o produto que escolheu: ')

    produto_selecionado = None
    for produto in enumerate(produtos_lista):
        print(produto[1][0])
        if produto[1][0] == escolha:
            produto_selecionado = produto[1][0]
            break

    if produto_selecionado is None:
        print('Produto selecionado não disponível')
    else:
        print(f'Produto disponível')

def cadastrar_produtos(produtos_lista):
    nome_produto = input('Favor informar o nome do novo produto: ')
    preco_produto = int(input('Favor informar o valor do novo produto: '))

    print(f'Produto: {nome_produto}, valor R$ {preco_produto}')

    produtos_lista.append((nome_produto, preco_produto))