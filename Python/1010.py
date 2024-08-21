iten = input().split(' ')
codigo = int(iten[0])
n_pecas = int(iten[1])
valor = float(iten[2])
total = n_pecas * valor

iten1 = input().split(' ')
codigo1 = int(iten1[0])
n_pecas1 = int(iten1[1])
valor1 = float(iten1[2])
total1 = n_pecas1 * valor1

pagamento = total1 + total

print(f'VALOR A PAGAR: R$ {pagamento:.2f}')