estudantes = {
    'nome': 'enzo',
    'idade': 18,
    'curso': 'tecnico em informatica'
}

arquivo = 'aquivo.txt'
lista = []

with open(arquivo, 'r')as arquivo:
    for chave, valor in estudantes.items():
        linha = f'{chave}: {valor}\n'
        lista.append(linha)

for i in lista:
    print(i)
