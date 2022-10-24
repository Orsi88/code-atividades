#Usando várias funções, faça um programa que verifique qual o valor de 6 itens que você deseja comprar em um supermercado: o primeiro terá o desconto de 3%, o segundo 3,5%, o terceiro 4,2%, o quarto 4,75%, o quinto 5,12% e o sexto 5,23%.

def recebendo_e_manipulando_valores():
    for cont in range(0, 6):
        produto = str(input('Qual o produto? '))
        preco = float(input('Informe o preço do produto: '))

        if cont == 0:
            precoNovo = preco - (preco * 0.03)
        elif cont == 1:
            precoNovo = preco - (preco * 0.035)
        elif cont == 2:
            precoNovo = preco - (preco * 0.042)
        elif cont == 3:
            precoNovo = preco - (preco * 0.0475)
        elif cont == 4:
            precoNovo = preco - (preco * 0.0512)
        elif cont == 5:
            precoNovo = preco - (preco * 0.0523)

        print('Com o desconto esse produto sairá por R${:.2f}'.format(precoNovo))
        cont += 1

recebendo_e_manipulando_valores()
