quantpontos = int(input('Quantos pontos você tem na carteira? '))

if quantpontos < 5:
    print('Bom condutor!')
elif quantpontos == 5:
    print('Bom condutor, tome cuidado!')
else:
    print('Condutor ruim, tome cuidado!')