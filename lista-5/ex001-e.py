def validacao_senha():

    # Coletando info

    senha = str(input('Digite a senha que deseja cadastrar: '))

    # Desmembrando senha

    partesSenha = []
    partesSenha.extend(senha)

    # Processo de Validação de Senha
    
    n = len(partesSenha)

    if n > 12 and n < 6:
       print('ERRO! Sua senha deve ter entre 6 e 12 caracteres!')
    else:
        print('SUa senha foi cadastrada com sucesso!')
    
    

    return

validacao_senha()