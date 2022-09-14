tempo = int(input('Por quanto tempo você irá aplicar? '))
valor = 1000
total = 0

for aplicacao in range(1, tempo+1):
    total = valor * 1.1
    print('{}º mês: {:.2f} * 1.1 = {:.2f}'.format(aplicacao, valor, total))
    valor = total

print('O valor final aplicado é de R${:.2f}'.format(total))