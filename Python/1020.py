x = int(input())

ano = x / 365
x %= 365

mes = x / 30
x %= 30

print(f'{int(ano)} ano(s)\n{int(mes)} mes(es)\n{int(x)} dia(as)')