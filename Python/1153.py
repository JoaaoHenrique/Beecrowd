x = int(input())

for y in range(x-1, 0, -1):
  z = x*y
  x = z
print(x)