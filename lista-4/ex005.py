valor = 100
tempo = 10
parcela = 0
soma = 0

for consorcio in range(1, tempo+1):
    parcela = valor * 1.02
    soma += parcela
    print('{}º parcela: R${:.2f}'.format(consorcio, parcela))
    valor = parcela

print('O valor que o último participante da lista vai receber é de R${:.2f}'.format(soma))