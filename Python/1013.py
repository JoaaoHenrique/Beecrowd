valores = input().split(' ')
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maior_ab = (a + b + abs(a - b))/2

maior = (maior_ab + c + abs(maior_ab - c))/2

resposta = int(maior)

print(f'{resposta} eh o maior')