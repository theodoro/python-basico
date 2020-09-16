#5. Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input('Informe um num:' ))
b = int(input('Informe um num:' ))
c = int(input('Informe um num:' ))

if a == b:
    print('O valor A é igual a B')
elif a == c:
    print('O Valor A é igual a C')
elif b == c:
    print('O valor B é igual a C')
elif a > b or a < b:
    if a > c and  a > b:
        print(str(a) + 'é maior que ' + str(b) + ',' + str(c))
    if a < c and a < b:
        print(str(a) + 'é menor que ' + str(b) + ',' + str(c))
elif b > a or b < a:
    if b > c and b > a:
        print(str(b) + 'é maior que ' + str(a) + ',' + str(c))
    if b < c and b < a:
        print(str(b) + 'é menor que ' + str(a) + ',' + str(c))
elif c > a or c < a:
    if c > b and c > a:
        print(str(c) + 'é maior que ' + str(a) + ',' + str(b))
    if c < b and c < a:
        print(str(c) + 'é menor que ' + str(a) + ',' + str(b))
