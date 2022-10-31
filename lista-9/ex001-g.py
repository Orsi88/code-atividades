#Crie um gráfico com o faturamento de vendas de uma loja dos últimos meses deste ano.

from string import ascii_letters, punctuation
from time import sleep

def shift_alf(alfab: str, shift: int) -> str:
        return alfab[shift:] + alfab[:shift]

def rot_algorithm(message: str, encryptionFlow: bool) -> str:
    alf = ascii_letters + punctuation
    if encryptionFlow == True:
        shift_alfabetos = shift_alf(alf, 17)
    else:
        shift_alfabetos = shift_alf(alf, -17)
    
    alf_final = ''.join(alf)
    shift_alf_final = ''.join(shift_alfabetos)
    tabela = str.maketrans(alf_final, shift_alf_final)
    return message.translate(tabela)

while True:

    print('''
        [1] Encriptar
        [2] Desencriptar
        [0] Encerrar
    ''')

    op = input('Opção: ').strip()
    if op == '1':
        mensagem = str(input('Digite uma mensagem: '))
        print(rot_algorithm(mensagem, True))
        sleep(0.5)

    elif op == '2':
        mensagem = str(input('Digite uma mensagem: '))
        print(rot_algorithm(mensagem, False))
        sleep(0.5)
    
    elif op == '0':
        print('Encerrando...')
        sleep(0.5)
        break

    else:
        print('Inválido.')
        sleep(0.3)

print('Fim')