valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

formula = ((b**2) - 4*a*c)

if a == 0 or formula < 0:
  print('Impossivel calcular')
else:
  formula = formula**0.5
  raiz1 = ((b * (-1)) + formula)/(2*a)
  raiz2 = ((b * (-1)) - formula)/(2*a)
  print(f'R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}')