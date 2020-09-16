velocidade = int(input('Informe a velociade KM: '))

if velocidade > 110:
    calc = velocidade - 110
    multa = calc * 5
    print(f'Multado! Você estava há {velocidade} o valor da multa é: ' + str(multa))
else:
    print('Velocidade Permitida!')
    
