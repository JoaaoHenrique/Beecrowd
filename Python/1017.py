tempo_viagem = int(input('Qual foi o tempo gasto na viagem: '))
velocidade_media = int(input('Qual foi a velocidade média dirante a viagem: '))

consumo = (velocidade_media/12) * tempo_viagem

print(f'{consumo:.3f}')