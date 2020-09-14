#3) Escreva um programa que leia a quantidade de dias, horas, minutos e
#segundos do usuário. Calcule o total em segundos.

d = int(input('Informe a quantidade de dias: '))
h = int(input('Informe a quantidade de Horas: '))
m = int(input('Informe a quantidade de Minutos: '))
s = int(input('Informe a quantidade de Segundos: '))

print((d * 86400) + (h * 3600) + (m * 60) + s)
