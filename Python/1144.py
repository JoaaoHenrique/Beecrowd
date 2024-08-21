x = int(input())
v = 1

for y in range(1, x+1):
  print(f'{v*1} {v**2} {v**3}')
  print(f'{v*1} {v**2+1} {v**3+1}')
  v += 1