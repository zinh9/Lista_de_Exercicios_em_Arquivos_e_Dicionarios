def info_ctt(lista_ctts):
    contato = {}
    
    while True:
        nome = input('Digite o nome do contato (digite "sair" para encerrar: ')
        
        if nome == 'sair':
            break
        
        tel = int(input('Digite o número de telefone com DDD: '))
        
        contato = {
            'Nome': nome,
            'Telefone': tel
        }
        
        lista_ctts.append(contato)
    
    return lista_ctts

def adicionar_arq(arq_ctts, lista_ctts):
    with open (arq_ctts, 'w') as arquivo:
        for contato in lista_ctts:
            arquivo.write(f'Nome: {contato["Nome"]}\n')
            arquivo.write(f'Telefone: {contato["Telefone"]}\n')
    
    return arq_ctts

def novo_ctt(arq_ctts, lista_ctts):
    nome = input('Digite o nome do contato: ')
    tel = int(input('Digite o número de telefone do contato com DDD: '))
    
    contato = {
        'Nome': nome,
        'Telefone': tel
    }
    
    lista_ctts.append(contato)
    
    with open (arq_ctts, 'a') as arquivo:
        for ctt in lista_ctts:
            arquivo.write(f'Nome: {ctt["Nome"]}\n')
            arquivo.write(f'Telefone: {ctt["Telefone"]}\n')
            
    return arq_ctts, lista_ctts
    
def mostrar(arq_ctts):
    with open (arq_ctts, 'r') as arquivo:
        for linha in arquivo:
            print(linha)

def atualizar(arq_ctts, lista_ctts):
    nome = input('Digite o nome do contato: ')
    
    for contato in lista_ctts:
        if nome == contato['Nome']:
            opcao = input('Digite a opção que deseja atualizar (nome/telefone ou nome e telefone): ')
        
            if opcao == 'nome':
                nome_at = input('Digite o novo nome do contato: ')
                
                contato['Nome'] = nome
            
            elif opcao == 'telefone':
                tel_at = int(input('Digite o novo número de telefone: '))
                
                contato['Telefone'] = tel_at
            
            elif opcao == 'nome' and opcao == 'telefone':
                nome_at = input('Digite o novo nome do contato: ')
                tel_at = int(input('Digite o novo número de telefone: '))
                
                contato['Nome'] = nome_at
                contato['Telefone'] = tel_at
        
        else:
            print('O nome não está no arquivo!')
    
    with open (arq_ctts, 'w') as arquivo:
        for contato in lista_ctts:
            arquivo.write(f'Nome: {contato["Nome"]}\n')
            arquivo.write(f'Telefone: {contato["Telefone"]}\n')
    
    return arq_ctts, lista_ctts

def remover(arq_ctts, lista_ctts):
    nome = input('Digite o nome do contato que deseja remover: ')
    
    for contato in lista_ctts:
        if nome == contato['Nome']:
            lista_ctts.remove(contato)
            print('O contato foi removido do arquivo!')
            
            with open(arq_ctts, 'w') as arquivo:
                for contato in lista_ctts:
                    arquivo.write(f'Nome: {contato["Nome"]}\n')
                    arquivo.write(f'Telefone: {contato["Telefone"]}\n')
        
        else:
            print('O nome não está no arquivo!')
    
    return arq_ctts, lista_ctts
    
def opcao(arq_ctts, lista_ctts):
    while True:
        resposta = input('Escolha uma das opções abaixo:\n\n4) Para adicionar um novo contato.\n3) Para visualizar os contatos.\n2) Para atualizar um contato do arquivo.\n1) Para remover um contato do arquivo.\n0) Para encerrar o programa\n\nOpção: ')
        
        if resposta == '4':
            arq_ctts, lista_ctts = novo_ctt(arq_ctts, lista_ctts)
        
        elif resposta == '3':
            mostrar(arq_ctts)
        
        elif resposta == '2':
            arq_ctts, lista_ctts = atualizar(arq_ctts, lista_ctts)
        
        elif resposta == '1':
            arq_ctts, lista_ctts = remover(arq_ctts, lista_ctts)
        
        elif resposta == '0':
            print('Obrigado :)')
            break
        
        else:
            print('Digite um dos números mencionados!')

lista_ctts = []
lista_ctts = info_ctt(lista_ctts)
arq_ctts = 'arquivo_contatos.txt'
arq_ctts = adicionar_arq(arq_ctts, lista_ctts)
opcao(arq_ctts, lista_ctts)
