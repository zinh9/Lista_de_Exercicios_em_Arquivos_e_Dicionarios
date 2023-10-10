def info_estudantes(lista_estudantes):
    estudante = {}

    while True:
        nome = input('Digite o nome do estudante (digite sair para encerrar): ')

        if nome == 'sair':
            break

        idade = int(input('Digite sua idade: '))
        curso = input('Digite seu curso: ')

        estudante = {
            'Nome': nome,
            'Idade': idade,
            'Curso': curso
        }

        lista_estudantes.append(estudante)
    
    return lista_estudantes

def adicionar_arq(arquivo_estudantes, lista_estudantes):
    with open (arquivo_estudantes, 'w') as arquivo:
        for estudante in lista_estudantes:
            arquivo.write(f'Nome: {estudante["Nome"]}\n')
            arquivo.write(f'Idade: {estudante["Idade"]}\n')
            arquivo.write(f'Curso: {estudante["Curso"]}\n')
    
    return arquivo_estudantes

def atualizar(arquivo_estudantes, lista_estudantes):
    nome = input('Digite o nome do estudante: ')

    for estudante in lista_estudantes:
        if nome == estudante['Nome']:
            opcao = input('Digite a opção que deseja atualizar (idade/curso ou idade e curso): ')

            if opcao == 'idade':
                idade_at = int(input('Digite a idade atualizada: '))

                estudante['Idade'] = idade_at

                print('A idade foi atualizada!')
            
            elif opcao == 'curso':
                curso_at = input('Digite o curso atualizado: ')

                estudante['Curso'] = curso_at

                print('O curso foi atualizado!')
            
            elif opcao == 'idade' and opcao == 'curso':
                idade_at = int(input('Digite a idade atualizada: '))
                curso_at = input('Digite o curso atualizado: ')

                estudante['Idade'] = idade_at
                estudante['Curso'] = curso_at

                print('A idade e o curso foram atualizados!')
    
        else:
            print('O estudante {nome} não está no arquivo!')
    
    with open (arquivo_estudantes, 'w') as arquivo:
        for estudante in lista_estudantes:
            arquivo.write(f'Nome: {estudante["Nome"]}\n')
            arquivo.write(f'Idade: {estudante["Idade"]}\n')
            arquivo.write(f'Curso: {estudante["Curso"]}\n')
    
    return arquivo_estudantes, lista_estudantes

def mostrar(arquivo_estudantes):
    nome = input('Digite o nome do estudante: ')
    estudante = {}
    lista_estudantes = []

    with open (arquivo_estudantes, 'r') as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(': ')
            estudante[chave] = valor
    
    lista_estudantes.append(estudante)

    for estudante in lista_estudantes:
        if nome == estudante['Nome']:
            print(f'Nome: {estudante["Nome"]}')
            print(f'Idade: {estudante["Idade"]}')
            print(f'Curso: {estudante["Curso"]}')

def opcao(arquivo_estudantes, lista_estudantes):
    while True:
        resposta = input('Segue as opções abaixo e escolha uma:\n\n2) Para visualizar o as informações do estudante pelo nome.\n1) Para atualizar os estudantes.\n0) Para encerrar o programa.\n\nOpção: ')

        if resposta == '2':
            mostrar(arquivo_estudantes)
            
        elif resposta == '1':
            arquivo_estudantes, lista_estudantes = atualizar(arquivo_estudantes, lista_estudantes)
        
        elif resposta == '0':
            print('Obrigado :)')
            break

        else:
            print('Digite um dos números mencionados!')

lista_estudantes = []
lista_estudantes = info_estudantes(lista_estudantes)
arquivo_estudantes = 'arquivo_estudantes.txt'
arquivo_estudantes = adicionar_arq(arquivo_estudantes, lista_estudantes)
opcao(arquivo_estudantes, lista_estudantes)
