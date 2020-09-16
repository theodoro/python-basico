#4. Faça um Programa que leia três números e mostre o maior deles.

a = int(input('Informe o numero A'))
b = int(input('Informe o numero B'))
c = int(input('Informe o numero C'))

if a > b and a > c:
    print('A é maior!')
elif b > a and b > c:
    print('B é o Maior!')
else:
    print('C é o maior:')
