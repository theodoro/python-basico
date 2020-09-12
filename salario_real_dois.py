salario = int(input('Salário?'))
imposto = input('Informe o % de imposto')

if imposto == '':
    imposto = 27.5
else:
    imposto = float(imposto)

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
