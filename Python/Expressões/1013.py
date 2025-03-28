x = input().split(' ')

a = int(x[0])
b = int(x[1])
c = int(x[2])

maiorAB = (a + b + abs(a - b))/2

maior = int((maiorAB + c + abs(maiorAB - c))/2)

print(f'{maior} eh o maior')

