nome = input('Qual o nome do funcionário: ').upper()
salario_fixo = float(input('Qual o salário fixo: '))
vendas = float(input('Qual foi o montante de vendas do funcionário: '))

bonus = (vendas * 0.15) + salario_fixo

print(f'TOTAL = R$ {bonus:.2f}')