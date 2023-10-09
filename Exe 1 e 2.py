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

def mostrar(arquivo_estudantes):
    with open (arquivo_estudantes, 'r') as arquivo:
        for linha in arquivo:
            print(linha)

def opcao(arquivo_estudantes):
    while True:
        resposta = input('Segue as opções abaixo e escolha uma:\n\n1) Para visualizar os estudantes.\n0) Para encerrar o programa.\n\nOpção: ')

        if resposta == '1':
            mostrar(arquivo_estudantes)
        
        elif resposta == '0':
            print('Obrigado :)')
            break

        else:
            print('Digite um dos números mencionados!')

lista_estudantes = []
lista_estudantes = info_estudantes(lista_estudantes)
arquivo_estudantes = 'arquivo_estudantes.txt'
arquivo_estudantes = adicionar_arq(arquivo_estudantes, lista_estudantes)
opcao(arquivo_estudantes)
