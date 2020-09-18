#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
#mensagem caso o valor seja inválido e continue pedindo até que o
#usuário informe um valor válido.


while True:
    nota = int(input('Informe uma nota: '))
    if nota > 0 and nota <=10:
        break
    else:
        print(f'Nota {nota} Inválida! Informe outra vez!')
print(f'Sua nota {nota:.1f}')
