def calculando_base16():
    print('Manipulando o Número 16')
    print('[1] Dobrar')
    print('[2] Tríplicar')
    print('[3] Quadruplicar')
    print('[4] Quíntuplicar')
    escolha = input('O que você deseja fazer com o número 16:')

    if escolha == '1':
        res = 16*2
    elif escolha == '2':
        res = 16*3
    elif escolha == '3':
        res = 16*4
    elif escolha == '4':
        res = 16*5
    return print('O resultado é {}'.format(res))

calculando_base16()
    