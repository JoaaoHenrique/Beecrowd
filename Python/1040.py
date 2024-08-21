n = input().split(' ')

n1 = float(n[0])
n2 = float(n[1])
n3 = float(n[2])
n4 = float(n[3])

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10
print(f'Media: {media:.1f}')

if media >= 7.0:
  print("Aluno aprovado.")
  
elif media < 5.0:
  print("Aluno reprovado.")

elif media >= 5.0 and media <= 6.9:
  print("Aluno em exame.")
  x = float(input())
  media_final = (x + media)/2
  print(f'Nota do exame: {x}')
  if media_final >= 5.0:
    print(f'Aluno aprovado.\nMedia final: {media_final:.1f}')
  else:
    print(f'Media: {media_final:.1f}\nAluno reprovado.')
