#Crie um dicionário com 6 nomes de pessoas e 6 CPF e imprima na tela.

cad = {
    'Nome': ['Nhee', 'Jubileu', 'Gege'],
    'CPF': ['33311122233', '99988877766', '333222244455']
}

n = {
    'ooo': 'welp'
}

for i in range(len(cad) + 1):
    for k, v in cad.items():
        if k == 'Nome':
            print(f'{k}: {v[i]}', end='   ')
        else:
            print(f'{k}: {v[i]}')

if len(cad['Nome']) > 2:
    print('Mais que 2 nomes')


if '33311122233' in cad['CPF']:
    print('Sim')
else:
    print('Não')

cad['CPF'][1] = '55566677788'
print(cad['CPF'])

n.pop('ooo')
n.pop('iii', 'Inexistente')

for i in range(len(cad['CPF'])):
    cad['CPF'][i] = cad['CPF'][i] + '*'
print(cad['CPF'])
