def adicionar_ctt(lista_ctt):
    ctt = {}
    
    while True:
        nome = input('Digite o nome do contato (digite sair para encerrar o programa): ')
        
        if nome == 'sair':
            break
        
        tel = int(input('Digite o número de telefone do contato (com DDD): '))
        
        ctt[nome] = tel
        lista_ctt.append(ctt)
    
    return lista_ctt
    
def salvar_ctts(lista_ctt, arq_ctt):
    with open(arq_ctt, 'w') as arquivo:
        for ctt in lista_ctt:
            for chave, valor in ctt.items():
                arquivo.write(f'{chave}: {valor}')
    
    print(f'Os contatos foram salvos no arquivo {arq_ctt}!')
    
    return arq_ctt

def adicionar(arq_ctt):
    nome = input('Digite o nome do contato: ')
    tel = int(input('Digite o número de telefone do contato (com DDD): '))
    
    with open(arq_ctt, 'a') as arquivo:
        arquivo.write(f'{nome}: {tel}')
    
    return arq_ctt

def visualizar(arq_ctt):
    with open(arq_ctt, 'r') as arquivo:
        for linha in arquivo:
            print(linha)

def atualizar(arq_ctt):
    nome = input('Digite o nome do contato que deseja atualizar: ')
    novo_tel = int(input('Digite o novo número de telefone do contato: '))
    ctt = {}
    ctts = []
    
    with open(arq_ctt, 'r') as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(': ')
            ctt[chave] = valor
    
    ctts.append(ctt)
    
    if nome not in ctts:
        print('O nome não está no arquivo!')
        return None
        
    for cont in ctts:
        for chave, valor in cont.items():
            if chave == nome:
                valor = novo_tel
                chave = valor
                break
    
    with open(arq_ctt, 'w') as arquivo:
        for cont in ctts:
            for chave, valor in cont.items():
                arquivo.write(f'{chave}: {valor}')
    
    print('O novo número de telefone foi atualizado no arquivo')
    
    return arq_ctt
    
lista_ctt = []
lista_ctt = adicionar_ctt(lista_ctt)
arq_ctt = 'arquivo_ctt.txt'
arq_ctt = salvar_ctts(lista_ctt, arq_ctt)

while True:
    resp = input('Segue as opções abaixo e escolha:\n\4) Para adicionar um novo contato.\n3) Para visualizar a lista de contatos.\n2) Para atualizar a lista de contatos.\n1) Para remover um contato.\n0) Para encerrar o programa')
    
    if resp == '4':
        arq_ctt = adicionar(arq_ctt)
    
    elif resp == '3':
        visualizar(arq_ctt)
    
    elif resp == '2':
        arq_ctt = atualizar(arq_ctt)
