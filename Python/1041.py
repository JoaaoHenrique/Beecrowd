z = input().split(' ')

x = float(z[0])
y = float(z[1])

if x == 0 and y == 0:
    print('Origem')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')
elif y < 0 and x > 0:
    print('Q4')
elif y > 0 and x > 0:
    print('Q1')
elif y < 0 and x < 0:
    print('Q3')
elif y > 0 and x < 0:
    print('Q2')