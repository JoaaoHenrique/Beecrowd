x = input().split(' ')
y = input().split(' ')

x2 = int(x[1])
x3 = float(x[2])

y2 = int(y[1])
y3 = float(y[2]) 

valorx = x2 * x3
valory = y2 * y3

valort = valorx + valory

print('VALOR A PAGAR: R$ {:.2f}'.format(valort))

