def separa():
    print('-*-'* 30)
def calculo_Comparacao():
    diaria = float(input('Qual o valor da diária? '))
    fixo = float(input('Qual o valor fixo? '))
    tempoDia = int(input('De quantos dias é a sua viagem? '))
    gastoTotal = (diaria * tempoDia) + fixo
    separa()
    return gastoTotal
def resposta():

    print('Orçamento 1:')
    plano1 = calculo_Comparacao()
    print('Orçamento 2:')
    plano2 = calculo_Comparacao()

    if plano1 > plano2:
        n = 1
        resp = plano2
    else:
        n = 2
        resp = plano1
    return print('O orçamento que mais compensa para o seu caso é o Nº{} que fica em um total de R${}'.format(n, resp))

separa()
resposta()
separa()



