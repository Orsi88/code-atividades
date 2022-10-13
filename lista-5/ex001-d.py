def calculo_desconto():

    #colhendo info

    nome = str(input('Digite seu nome: '))
    salario = float(input('Digite o valor bruto do seu dalário: '))

    #cálculo desconto INSS

    if salario < 1751.81:
        impostoInss = salario * 0.08
    elif salario < 2919.72 and salario > 1751.81:
        impostoInss = salario * 0.09
    elif salario < 5839.45 and salario >2919.72:
        impostoInss = salario * 0.11

    #cálculo desconto Imposto de Renda

    if salario < 1903.98:
        impostoIr = 0
    elif salario < 2826.65 and salario > 1903.98:
        impostoIr = salario * 0.075
    elif salario < 3751.05 and salario > 2826.65:
        impostoIr = salario * 0.15
    elif salario < 4664.68 and salario > 3751.05:
        impostoIr = salario * 0.225
    elif salario > 4664.68:
        impostoIr = salario * 0.275

    #cálculo desconto final

    descontoTotal = salario - (impostoInss + impostoIr)
    res = print('Olá, {}! O seu salário líquido é de R${}!'.format(nome, descontoTotal))
    
    return


#Código

calculo_desconto()
