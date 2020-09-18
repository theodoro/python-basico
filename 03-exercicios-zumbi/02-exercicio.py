#2. Faça um programa que leia um nome de usuário e a sua senha e não
#aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro
#e voltando a pedir as informações.


while True:
    usuario = input('Informe um Login: ')
    senha = input('Senha: ')

    if usuario == senha:
        print('Usuário ou senha inválidos, por favor, repetir')
    else:
        break
print('Usuário cadastrado com sucesso!!')

