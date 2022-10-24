#Faça um programa com a variável global ano = 2019. Crie funções que calcule a idade de várias pessoas, enquanto não digitar 0000 para finalizar o programa. Uma função será para mostrar a idade menor que 18 anos; a segunda, para mostrar a idade menor ou igual a 30 anos; a terceira para mostrar a idade menor que 50 anos; a quarta para mostrar a idade menor que 80 anos.

ano = 2019
nome = ''
aniversario = [2099]
escolha = '0001'
deMenor = []
criseDos30 = []
criseMeiaIdade = []
naFlorDaIdade = []

def recebendo_info():
    nome = str(input('Qual o seu nome? '))
    aniversario = int(input('Em que ano você nasceu? '))
    return nome, aniversario

def manipulando_info():
    for escolha in range (escolha != '0000'):
        recebendo_info()

        if 2019 - aniversario < 18:
            deMenor.append(nome)
        elif 2019 - aniversario <= 30:
            criseDos30.append(nome)
        elif 2019 - aniversario < 50:
            criseMeiaIdade.append(nome)
        elif 2019 - aniversario < 80:
            naFlorDaIdade.append(nome) 

        escolha = str(input('Deseja realizar outro cadastro [0001] - Sim [0000] - Não: '))
        
        return print(deMenor), print(criseDos30), print(criseMeiaIdade), print(naFlorDaIdade)

        

manipulando_info()
