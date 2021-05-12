from random import randint

a = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

ordem = sorted(a)

print('Os valores sorteados foram:', end = ' ')

for n in a:
    print(f'{n}', end = ' ')

print(f'\n\nO menor valor sorteado foi {min(a)}\nO maior valor sorteado foi {max(a)}\n\n')
