nome = str(input('Qual o seu nome? '))
idade = int(input('Quantos anos você tem? '))
print('{} tem {} anos!'.format(nome, idade))

print('A variável "nome" está no endereço ', hex(id(nome)))
print('A variável "idade" está no endereço', hex(id(idade)))
