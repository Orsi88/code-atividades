valordacompra = 637.78

if valordacompra > 150:
    valorcomdesconto = valordacompra * 0.90
    print('Valor com desconto de 10%: R${}'.format(valorcomdesconto))
elif valordacompra == 150:
    valorcomdesconto = valordacompra * 0.93
    print('Valor com desconto de 7%: R${}'.format(valorcomdesconto))
else:
    valorcomdesconto = valordacompra * 0.96
    print('Valor com desconto de 4%: R${}'.format(valorcomdesconto))