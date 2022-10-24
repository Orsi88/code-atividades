#Faça um programa, usando funções que mostre, dentro de 4 funções com senha de administrador, separadas, se a senha digitada pelo usuário é válida ou não.
status = ['ok', 'ok', 'ok', 'ok']
def etapa_1():
    if numeroCaracteres < 6:
        status.append('negado')
        status.remove('ok')
        return print('SENHA INVÁLIDA! Sua senha deve ter mais que 6 caracteres.'), status
     
def etapa_2():
    if not any(x.isupper() for x in partesSenha):
        status.append('negado')
        status.remove('ok')
        return print('SENHA INVÁLIDA! Deve conter pelo menos uma letra maiúscula.'), status

def etapa_3():
    if not any(x.islower() for x in partesSenha):
        status.append('negado')
        status.remove('ok')
        return print('SENHA INVÁLIDA! Deve conter pelo menos uma letra minúscula.'), status
     

def etapa_4(): 
    if all(x.isdigit() == False for x in partesSenha):
        status.append('negado')
        status.remove('ok')
        return print('SENHA INVÁLIDA! Deve conter pelo menos um número.'), status
     

# Recebendo info

senha = str(input('Digite a senha que deseja cadastrar: '))

# Desmembrando senha

partesSenha = []
partesSenha.extend(senha)

# Processo de Validação de Senha
    
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numeroCaracteres = len(partesSenha)

etapa_1()
etapa_2()
etapa_3()
etapa_4()
if status == ['ok', 'ok', 'ok', 'ok']:
    print('SENHA VÁLIDA! Sua senha foi cadastrada com sucesso.')
    
   