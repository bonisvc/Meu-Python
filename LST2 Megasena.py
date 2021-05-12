from random import randint
from time import sleep

print('='*40, end = '\n')
print(f'{"GERADOR DE JOGOS DA MEGASENA":^40}')
print('='*40, end = '\n\n')

n = int(input('Quantas Surpresinhas você deseja jogar? '))

print('\nProcessando...\n\n')
sleep(3)

l = []
c = 0

while c < n: 
    for x in range(0, 6):
        y = randint(1, 60)
        if l.count(y) != 0:
            y = randint(1, 60)
            l.append(y)
        else:
            l.append(y)
    c += 1
    print(f'Jogo {c}: {sorted(l)}')
    sleep(1)
    l.clear()

print('_'*40, end = '\n')
print(f'{"BOA SORTE!!!":^40}')
print('='*40, end = '\n')
    