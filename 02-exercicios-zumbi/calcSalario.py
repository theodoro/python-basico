#6. Faça um Programa que pergunte quanto você ganha por hora e o número
#de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
#referido mês, sabendo-se que são descontados 11% para o Imposto de
#Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
#dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o
#salário líquido. Observe que Salário Bruto - Descontos = Salário
#Líquido. Calcule os descontos e o salário líquido, conforme a tabela
#abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

valorHora = float(input('Informe o valor da hora trabalhada :'))
horasTrab = float(input('Informe a quantiade de horas trabalhadas ;'))

bruto = valorHora * horasTrab
print (f'Salário Bruto : R${bruto}')

ir = bruto * 0.11
print (f'IR (11%) : R${ir}')

inss = bruto * 0.08
print(f'INSS (8%) : R${inss}')

sind = bruto * 0.05
print(f'indicato ( 5%) : R${sind}')

descontos = (ir + inss + sind)
liquido = bruto - descontos
print(f'Salário Liquido : R${liquido}')

