gasolina = float(input('Informe o preço da Gasolina :'))
etanol = float(input('Informe o preço do Etanol :'))

divisao = etanol / gasolina

if divisao < 0.7:
    print('Abastecer com Etanol')
else:
    print('Abastecer com Gasolina')
