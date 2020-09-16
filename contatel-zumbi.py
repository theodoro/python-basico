minutos = int(input('Quantidade de minutos utilizados :'))

if minutos < 200:
    calc = (200 - minutos) * 0.20
    print(f'Quantidade{minutos} e a Tarifa : ' + str(calc))
if minutos >= 200 and minutos <= 400:
    calc = (minutos - 200) * 0.18
    print(f'Quantidade{minutos} e a Tarifa : ' + str(calc))
if minutos > 400 and minutos <= 800:
    calc = (minutos - 200) * 0.15
    print(f'Quantidade{minutos} e a Tarifa : ' + str(calc))
if minutos > 800:
    calc = (minutos - 200) * 0.08
    print(f'Quantidade{minutos} e a Tarifa : ' + str(calc))
