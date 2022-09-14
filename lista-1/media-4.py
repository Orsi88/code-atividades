from dataclasses import replace


numero1 = int (input('Informe o primeiro número: '))
numero2 = int (input('Informe o segundo número: '))
numero3 = int (input('Informe o terceiro número: '))
numero4 = int (input('Informe o quarto número: '))

soma = numero1 + numero2 + numero3 + numero4
media = (soma/4)

print('A média dos quatro valores é: ',str(media).replace ('.',','))