#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba
#o valor do desconto e o preço a pagar.

preco = float(input('Informe o preço do produto: '))
desconto = float(input('Informe o desconto: '))

calcDesc = (preco * desconto) /100

print('Valor Desconto: ' + str(calcDesc))
print('Preço final: ' + str(preco - calcDesc))
