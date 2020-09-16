#2. Determine se um ano é bissexto. Verifique no Google como fazer isso...

ano = int(input('Informe o ano :'))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('Ano Bissexto')
else:
    print('Não é Bissexto')
