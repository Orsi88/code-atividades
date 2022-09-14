a = 8
b = 3

soma = a + b
subtracao = a - b
divisao = a/b
mutiplicacao = a * b
divisaoInteira = a // b
resto = a % b

print('Resultado soma: {}'.format(soma))
print('Endereço da variável "soma": ', hex(id(soma)))

print('Resultado subtração: {}'.format(subtracao))
print('Endereço da variável "subtracao": ', hex(id(subtracao)))

print('Resultado divisão: {}'.format(divisao))
print('Endereço da variável "divisao": ', hex(id(divisao)))

print('Resultado mutiplicação: {}'.format(mutiplicacao))
print('Endereço da variável "mutiplicacao": ', hex(id(mutiplicacao)))

print('Resultado Divisão Inteira: {}'.format(divisaoInteira))
print('Endereço da variável "divisaoInteira": ', hex(id(divisaoInteira)))

print('Resultado Resto: {}'.format(resto))
print('Endereço da variável "resto": ', hex(id(resto)))