numero = int(input('Qual o número do funcionário: '))
horas_t = int(input('Quantas horas ele trabalhou esse mês: '))
salario_hora = float(input('Qual o salário por hora desse funcionário: '))

salario = (horas_t * salario_hora)

print(f'NUMBER = {numero}\nSALARY = U$ {salario:.2f}')