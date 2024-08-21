x = int(input())

print(x)

cem = x / 100
x %= 100

cinquenta = x / 50
x %= 50

vinte = x /20
x %= 20

dez = x / 10
x %= 10

cinco = x / 5
x %= 5

dois = x / 2
x %= 2

um = x / 1
x %= 1

print(f'{int(cem)} nota(s) de R$ 100,00')
print(f'{int(cinquenta)} nota(s) de R$ 50,00')
print(f'{int(vinte)} nota(s) de R$ 20,00')
print(f'{int(dez)} nota(s) de R$ 10,00')
print(f'{int(cinco)} nota(s) de R$ 5,00')
print(f'{int(dois)} nota(s) de R$ 2,00')
print(f'{int(um)} nota(s) de R$ 1,00')