#Faça um programa com a variável global ano = 2019. Crie funções que calcule a idade de várias pessoas, enquanto não digitar 0000 para finalizar o programa. Uma função será para mostrar a idade menor que 18 anos; a segunda, para mostrar a idade menor ou igual a 30 anos; a terceira para mostrar a idade menor que 50 anos; a quarta para mostrar a idade menor que 80 anos.

anoAtual =2019
faixa1 = []
faixa2 = []
faixa3 = []
faixa4 = []

def recolhendo_dados():
    nome = str(input('Qual o seu nome?'))
    anoNascimento = int(input('Em que ano você nasceu? '))

    if 2019 - anoNascimento < 18:
        faixa1.append(nome)
        print('Você é de menor!')
    elif 2019 - anoNascimento <= 30:
        faixa2.append(nome)
        print('Você esta na crise dos 30 ?!! kkkk')
    elif 2019 - anoNascimento < 50:
        faixa3.append(nome)
        print('Você esta na crise da meia idade! :)')
    elif 2019 - anoNascimento < 80:
        faixa4.append(nome)
        print('Você esta na flor da idade! S2')

while

print('-=-'*15)
print('ANALISE...')
print('{} menor de 18 anos'.format(faixa1))
print('{} tem 30 anos ou menos'.format(faixa2))
print('{} tem menos de 50 anos'.format(faixa3))
print('{} tem menos de 80 anos'.format(faixa4))
print('-=-'*15)