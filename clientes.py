def cadastrar_cliente(clientes_lista): 
    nome_cliente = input('Por favor, diga seu nome desejado: ')
    if nome_cliente == '':
        print('O nome está em branco')  
    else:
        clientes_lista.append(nome_cliente)
    
def listar_cliente(clientes_lista): 
    for cliente in clientes_lista:
        print(cliente)  