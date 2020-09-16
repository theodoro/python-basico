#1. Faça um Programa que peça os três lados de um triângulo. O programa
#deverá informar se os valores podem ser um triângulo. Indique, caso os
#lados formem um triângulo, se o mesmo é: equilátero, isósceles ou
#escaleno.


a = int(input('Informe o lado A :'))
b = int(input('Informe o lado B :'))
c = int(input('Informe o lado C :'))

if a > b + c or b > a + c or c > a + b:
  print ('Não pode ser um triângulo')
  print ('Um dos lados é maior que a soma dos outros') 
elif a != b and a != c and b != c:
    print('Escaleno!')
elif a == b or a == c or b == c:
    print('Isosceles')
elif a == b and a == c and b ==c:
    print('Equilatero')
else:
    print('Não é um triangulo!')
