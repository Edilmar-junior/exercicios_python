"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações. Faça um programa que leia e valide as seguintes informações: """

condicao = True
while condicao:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if senha != login:
        print('Parabéns sua senha foi cadastrada com sucesso! ')
        break
    else:
        print('Senha cadastrada igual ao login não é possivel!')
        continue
        