#1. Pelo menos 1 letra entre [a-z]
#2. Pelo menos 1 número entre [0-9]
#3. Pelo menos 1 letra maiúscula [A-Z] 
#4. Número mínimo de caracteres: 6
#5. Número máximo de caracteres: 12

from tokenize import Number


def validacao_senha():

    # Coletando info

    senha = str(input('Digite a senha que deseja cadastrar: '))

    # Desmembrando senha

    partesSenha = []
    partesSenha.extend(senha)

    # Processo de Validação de Senha
    
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numeroCaracteres = len(partesSenha)

    if numeroCaracteres > 12 and numeroCaracteres < 6:
      res = print('ERRO! Sua senha deve ter entre 6 e 12 caracteres!')
    # Tem que ter uma forma de ler a senha e identificar separado tipo index, index é uma possibilidade assim como any
    #elif any([x == Number for x in numeros]):
      #res = print('ERRO! Sua senha deve ter pelo menos um número!')
    else:
      res = print('Sua senha foi cadastrada com sucesso!')

    return res

validacao_senha()