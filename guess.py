import random

print('-----------------------------------')
print('Bem-vindo(a) ao jogo da adivinhação')
print('-----------------------------------\n')

numero_secreto = random.randrange(1, 101)
total_de_tentavivas = 0
pontos = 1000

print('Esses serão os níveis de dificuldade:', '1. Fácil', '2. Médio', '3. Difícil', sep='\n')

#Definindo as tentaivas por nível de didiculdade
nivel = int(input('Selecione o nível de dificuldade desejado: '))
if nivel == 1:
    total_de_tentavivas = 20
elif nivel == 2:
    total_de_tentavivas = 10
else:
    total_de_tentavivas = 5

#Definindo as rodadas
for rodada in range(1, total_de_tentavivas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentavivas))
    chute = input('Digite um número entre 1 e 100: ')
    print('Você chutou o número', chute)
    chute = int(chute)

    if chute < 1 or chute > 100:
        print('Número inválido')
        continue

    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acerto:
        print('Parabéns! Você acertou o número secreto', 'Você fez {} pontos!\n'.format(pontos), sep='\n')
        break

    else:
        if maior:
            print('Você errou! O número secreto é menor do que {}'.format(chute))
        elif menor:
            print('Você errou! O número secreto é maior do que {}'.format(chute))
        pontos_perdidos = abs(numero_secreto - chute) #abs significam números absolutos
        pontos = pontos - pontos_perdidos

print('GAME OVER')
print('*********')

