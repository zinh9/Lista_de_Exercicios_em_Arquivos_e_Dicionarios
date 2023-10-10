import csv

def compras(lista_compras):
    compra = {}

    while True:
        produto = input('Digite o nome do produto (digite "sair" para encerrar): ')

        if produto == 'sair':
            break

        preco = float(input('Digite o preço do produto: '))

        compra[produto] = preco

        lista_compras.append(compra)
    
    return lista_compras

def adicionar_arq(arquivo_compras, lista_compras):
    with open (arquivo_compras, 'w') as arquivo:
        for compra in lista_compras:
            for produto, preco in compra.items():
                arquivo.write(f'{produto}: {preco}\n')
    
    return arquivo_compras

def nova_compra(arquivo_compras, lista_compras):
    compra = {}
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))

    compra[produto] = preco

    lista_compras.append(compra)

    with open (arquivo_compras, 'a') as arquivo:
        for novo in lista_compras:
            for novo_produto, novo_preco in novo.items():
                arquivo.write(f'{novo_produto}: {novo_preco}\n')
    
    return arquivo_compras, lista_compras

def atualizar_preco(arquivo_compras, lista_compras):
    nome_produto = input('Digite o nome do produto que deseja atualizar o preço: ')

    for compra in lista_compras:
        for produto, preco in compra.items():
            if nome_produto == produto:
                novo_preco = float(input('Digite o novo preço do produto: '))
                preco = novo_preco
                compra[produto] = preco

                with open (arquivo_compras, 'w') as arquivo:
                    for compra in lista_compras:
                        for produto, preco in compra.items():
                            arquivo.write(f'{produto}: {preco}\n')

        else:
            print('O produto não está no arquivo!')
    
    return arquivo_compras, lista_compras

def valor_total(lista_compras):
    total = []

    for compra in lista_compras:
        for produto, preco in compra.items():
            if preco not in total:
                total.append(preco)
    
    print(f'O preço total dos produtos do arquivo é: R${sum(total)}')

def opcao(arquivo_compras, lista_compras):
    while True:
        resposta = input('Escolha uma das opções abaixo:\n\n3) Para adicionar um novo produto.\n2) Para atualizar o valor de um produto.\n1) Para ver o valor total das compras.\n0) Para encerrar o programa\n\nOpção: ')

        if resposta == '3':
            arquivo_compras, lista_compras = nova_compra(arquivo_compras, lista_compras)
        
        elif resposta == '2':
            arquivo_compras, lista_compras = atualizar_preco(arquivo_compras, lista_compras)
        
        elif resposta == '1':
            valor_total(lista_compras)
        
        elif resposta == '0':
            print('Obrigado :)')
            break
        
        else:
            print('Digite uma das opções mencionadas!')

lista_compras = []
lista_compras = compras(lista_compras)
arquivo_compras = 'arquivo_compras.csv'
arquivo_compras = adicionar_arq(arquivo_compras, lista_compras)
opcao(arquivo_compras, lista_compras)
