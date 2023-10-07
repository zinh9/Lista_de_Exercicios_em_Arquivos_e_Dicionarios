def pedir_infor(estudantes):
    while True:
        nome = input('\nDigite seu nome (digite "sair" para encerrar): ')
        
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
    
    print(f'\nAs informações foram salvas no arquivo {arquivo_estudantes}.')
    
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
        nome = input('\nDigite seu nome (digite sair para encerrar): ')
        
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
        
    print(f'\nO arquivo {arquivo_estudantes} foi atualizado!')
    
    return arquivo_estudantes

def consultar(arquivo_estudantes):
    nome = input('\nDigite o nome do estudante: ')
    estudantes = []

    with open(arquivo_estudantes, 'r') as arquivo:
        estudante = {}
        for linha in arquivo:
            chave, valor = linha.strip().split(': ')
            estudante[chave] = valor
            if chave == 'Curso':
                estudantes.append(estudante.copy())
                estudante.clear()
    
    encontrado = False
    
    for estudante in estudantes:
        if estudante.get('Nome') == nome:
            encontrado = True
            print(f'Nome: {estudante.get("Nome", "N/A")}')
            print(f'Idade: {estudante.get("Idade", "N/A")}')
            print(f'Curso: {estudante.get("Curso", "N/A")}\n')
    
    if not encontrado:
        print('\nO estudante não se encontra no arquivo!')

def remover(arquivo_estudantes):
    nome = input('\nDigite o nome do estudante que deseja remover: ')
    estudante = {}
    estudantes = []
    removido = None
    
    with open(arquivo_estudantes, 'r') as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(': ')
            estudante[chave] = valor
            
    estudantes.append(estudante)
    
    for estudant in estudantes:
        if estudant['Nome'] == nome:
            removido = estudant
            break
    
    if removido:
        estudantes.remove(removido)
        
        with open(arquivo_estudantes, 'w') as arquivo:
            for estudant in estudantes:
                arquivo.write(f'Nome: {estudant["Nome"]}')
                arquivo.write(f'Idade: {estudant["Idade"]}')
                arquivo.write(f'Curso: {estudant["Curso"]}')
        
        print(f'\nO estudante {nome} foi removido!')
    
    else:
        print('\nO estudante não está no arquivo!')
    
    return arquivo_estudantes

def media_idade(arquivo_estudantes):
    media = 0
    estudante = {}
    idades = []
    
    with open(arquivo_estudantes, 'r') as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(': ')
            
            if chave == 'Idade':
                idades.append(int(valor))
    
    media = sum(idades) / len(idades)
        
    print(f'\nA média das idades dos estudantes é de {int(media)} anos!')

def estudantes_curso(arquivo_estudantes):
    cursos_alunos = {}
    
    with open(arquivo_estudantes, 'r') as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(': ')
            
            if chave == 'Curso':
                curso = valor
                
                if curso not in cursos_alunos:
                    cursos_alunos[curso] = 0
                cursos_alunos[curso] += 1
    
    for curso, num_alunos in cursos_alunos.items():
        print(f'Curso: {curso}, Número de Alunos: {num_alunos}')
    
estudantes = []
estudantes = pedir_infor(estudantes)
arquivo_estudantes = 'arquivo_est.txt'
arquivo_estudantes = salvar_arquivo(arquivo_estudantes, estudantes)

while True:
    resposta = input('\nSobre o arquivo, escolha uma das opções abaixo e digite a opção:\n\n6) Para ver quantos estudantes tem em cada curso.\n5) Para ver a média das idades dos estudantes.\n4) Para remover um estudante do arquivo.\n3) Para consultar um estundate pelo nome para ver suas informações.\n2) Para visualizar o arquivo todo.\n1) Para adicionar um novo estudante.\n0) Para encerrar o programa.\n\nOpção: ')
    
    if resposta == '6':
        estudantes_curso(arquivo_estudantes)
        
    elif resposta == '5':
        media_idade(arquivo_estudantes)
        
    elif resposta == '4':
        remover(arquivo_estudantes)
        
    elif resposta == '3':
        consultar(arquivo_estudantes)
        
    elif resposta == '2':
        mostrar_arquivo(arquivo_estudantes)
    
    elif resposta == '1':
        atualizar_arquivo(arquivo_estudantes)
    
    elif resposta == '0':
        print('Obrigado :)')
        break
