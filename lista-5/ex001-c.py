def calculo_juros(tempo):
    totalConta = valor * juros * tempo
    print('O valor com o juros após {} mês é de R${:.2f}'.format(tempo, totalConta))

def tempo_limite(totalConta):
    tempo = (valor * juros)/totalConta
    print('Em {:.2f} meses o valor da conta ultrapassará R$ 160,00.'.format(tempo))

def dobradinha():
    tempo = (valor * juros)/valor*2
    print('Em {:.2f} meses o valor da conta terá dobrado.'.format(tempo))

#-------------------------------------------------------------------

valor = 134
juros = 1.03

calculo_juros(1)
calculo_juros(3)
tempo_limite(160)
dobradinha()








    


        




