#4) Faça um programa que calcule o aumento de um salário. Ele deve
#solicitar o valor do salário e a porcentagem do aumento. Exiba o valor
#do aumento e do novo salário.

salario = float(input('Informe o valor do Salário: '))
aumento = float(input('Informe o % de aumento: '))

print('Aumento: ' + str((salario * aumento)/100))
print('Novo Salário: ' + str(salario + (salario * aumento)/100))
