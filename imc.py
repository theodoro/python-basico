peso = float(input('Informe seu Peso :'))
altura = float(input('Informe sua altura :'))

imc = (altura * altura) / peso

if imc >= 18.5 and imc <= 24.9:
    print('Peso Normal')
elif imc >= 25 and imc <= 29.9:
    print('Acima do Peso')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau 1')
elif imc >= 35 and imc <= 40:
    print('Obesidade Grau 2')
else:
    print('Peso invalido')
