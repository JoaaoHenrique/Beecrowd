x = int(input())

a, b = 0, 1

for y in range(x - 1):
  print(a, end=' ')
  a, b = b, b+a
print(a)