def pedir_infor(estudantes):
    while True:
        nome = input('Digite seu nome (digite "sair" para encerrar): ')
        
        if nome.lower() == 'sair':
            break
        
        idade = int(input('Digite sua idade: '))
        curso = input('Digite o curso: ')
        
        estudante = {
            'Nome': nome,
            'Idade': idade,
            'Curso': curso
        }
        
        estudantes.append(estudante)
        
    return estudantes

def salvar_arquivo(arquivo_estudantes, estudantes):
    with open(arquivo_estudantes, 'w') as arquivo:
        for estudante in estudantes:
            arquivo.write(f'Nome: {estudante["Nome"]}\n')
            arquivo.write(f'Idade: {estudante["Idade"]}\n')
            arquivo.write(f'Curso: {estudante["Curso"]}\n')
    
    print(f'As informações foram salvas no arquivo {arquivo_estudantes}')
    
    return arquivo_estudantes

def mostrar_arquivo(arquivo_estudantes):
    with open(arquivo_estudantes, 'r') as arquivo:
        for linha in arquivo:
            print(linha)


def atualizar_arquivo(arquivo_estudantes):
    estudante = {}
    estudantes = []
    
    with open(arquivo_estudantes, 'r') as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(': ')
            estudante[chave] = valor
        
    while True:
        nome = input('Digite seu nome (digite sair para encerrar): ')
        
        if nome == 'sair':
            break
            
        idade = int(input('Digite sua idade: '))
        curso = input('Digite seu curso: ')
            
        estudante = {
            'Nome': nome,
            'Idade': idade,
            'Curso': curso
        }
            
        estudantes.append(estudante)
        
    with open(arquivo_estudantes, 'a') as arquivo:
        for estudant in estudantes:
            arquivo.write(f'Nome: {estudant["Nome"]}\n')
            arquivo.write(f'Idade: {estudant["Idade"]}\n')
            arquivo.write(f'Curso: {estudant["Curso"]}\n')
        
    print(f'O arquivo {arquivo_estudantes} foi atualizado!')
    
estudantes = []
estudantes = pedir_infor(estudantes)
arquivo_estudantes = 'arquivo_est.txt'
arquivo_estudantes = salvar_arquivo(arquivo_estudantes, estudantes)

while True:
    resposta = input('Digite 2 para verificar o arquivo, 1 para atualizar o arquivo, ou 0 para encerrar o programa: ')
    
    if resposta == '2':
        mostrar_arquivo(arquivo_estudantes)
    
    elif resposta == '1':
        atualizar_arquivo(arquivo_estudantes)
    
    elif resposta == '0':
        print('Obrigado :)')
        break
