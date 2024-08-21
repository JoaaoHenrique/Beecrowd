x = int(input())

horas = x / 3600
x %= 3600

minutos = x / 60
x %= 60

segundos = x

print(f'{int(horas)}:{int(minutos)}:{int(segundos)}')