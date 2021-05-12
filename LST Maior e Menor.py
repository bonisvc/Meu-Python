l = []
maior = menor = 0

for n in range(0, 5):
    l.append(int(input('Digite um número: ')))
    if n == 0:
        maior = l[n]
        menor = l[n]
    if l[n] > maior:
        maior = l[n]
    if l[n] < menor:
        menor = l[n]

print(f'Você digitou os números: {l}')

print(f'\nO maior número encontrado foi o {maior} na posição: ', end = ' ')

for x, y in enumerate(l):
    if y == maior:
        print(f'... {x}', end = ' ')

print(f'\nO menor número encontrado foi o {menor} na posição: ', end = ' ')

for x, y in enumerate(l):
    if y == menor:
        print(f'... {x}', end = ' ')