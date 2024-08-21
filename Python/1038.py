x = int(input())
y = int(input())

x = str(x)

lanches = {'1':4.00, '2':4.50, '3':5.00, '4':2.00, '5':1.50}

if x in lanches:
  codigo = lanches[x]
  total = codigo * y
  print(f'Total: R$ {total:.2f}')