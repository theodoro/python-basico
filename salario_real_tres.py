salario = int(input('Salário?'))
imposto = input('Imposto em %')

if not imposto:
    imposto = 27.8
else:
    imposto = float(imposto)

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))