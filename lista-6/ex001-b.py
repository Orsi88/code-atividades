#Usando várias funções, faça um programa que verifique qual o valor de 6 itens que você deseja comprar em um supermercado: o primeiro terá o desconto de 3%, o segundo 3,5%, o terceiro 4,2%, o quarto 4,75%, o quinto 5,12% e o sexto 5,23%.
listaProdutos = []
listaValores = []
listaDescontos = [0.03, 0.035, 0.042, 0.0475, 0.0512, 0.0523]



def recolhendo_info():
    for cont in range(1, 4):
        produto = input('Adicione o {}º produto a lista: '.format(cont))
        valor = float(input('Informe o preço: '))

        listaProdutos.insert(-1, produto)
        listaValores.insert(-1, valor)
        cont +=1

def adicionando_descontos():
    recolhendo_info()
    for cont in range(1, 4):
        novoValor = listaValores[-1] * 0.03
        cont +=1
        print(listaNovosValores)
    

adicionando_descontos()