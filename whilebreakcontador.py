soma = 0
contador = 0

while True:
    x = int(input('n (Zero para sair):'))
    if x == 0:
        break
    soma = soma + x
    contador = contador + 1
print(f'Soma: {soma} Média: {soma/contador:.1f}')
