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
    resposta = input('Deseja verificar o arquivo (sim/não) ? ')
    
    if resposta == 'sim':
        with open(arquivo_estudantes, 'r') as arquivo:
            for linha in arquivo:
                print(linha)
    
    else:
        return None
    
estudantes = []
estudantes = pedir_infor(estudantes)
arquivo_estudantes = 'arquivo_est.txt'
arquivo_estudantes = salvar_arquivo(arquivo_estudantes, estudantes)
mostrar_arquivo(arquivo_estudantes)
