salario = []
i = 0
soma = 0

while i <= 3:
    salario.append(float(input('Salário :')))
    soma = soma + salario[i]
    i = i + 1
print(f'Média {salario} é {soma/12:.1f}')
