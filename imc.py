peso = float(input('Informe seu Peso :'))
altura = float(input('Informe sua altura :'))

imc = peso / (altura * 2)

if imc >= 18.5 and imc <= 24.9:
    print('Peso Normal {imc}' + str(imc))
elif imc >= 25 and imc <= 29.9:
    print('Acima do Peso {imc}' + str(imc))
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau 1 {imc}' + str(imc))
elif imc >= 35 and imc <= 40:
    print('Obesidade Grau 2 {imc}' + str(imc))
else:
    print('Peso invalido {imc}' + str(imc))
