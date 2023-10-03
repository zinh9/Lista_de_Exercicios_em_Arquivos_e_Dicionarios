estudantes = {
    'nome': 'enzo',
    'idade': 18,
    'curso': 'tecnico em informatica'
}

arquivo = 'aquivo.txt'

with open(arquivo, 'w')as arquivo:
    for chave, valor in estudantes.items():
        linha = f'{chave}: {valor}\n'
        arquivo.write(linha)

print(f'O dicionario foi escrito nesse arquivo {arquivo}')
