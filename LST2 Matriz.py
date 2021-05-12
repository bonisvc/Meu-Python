'''l = []

for c in range(0, 9):
    l.append(int(input(f'Digite o [{c + 1}° número: ')))

pos = 0

while pos < len(l):
    if pos == 0 or (pos + 1) % 3 != 0:
        print(f'{l[pos]:^2}', end = ' ')
    else:
        print(f'{l[pos]:^2}', end = '\n')
    pos += 1

d = (l[0] * l[4] * l[8] + l[1] * l[5] * l[6] + l[2] * l[3] * l[7]) - (l[2] * l[4] * l[6] + l[1] * l[3] * l[8] + l[0] * l[5] * l[7])

print(f'O determinante da matriz dada é: {d}')'''

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range (0, 3):
        m[l][c] = int(input(f'Digite o ({l + 1},{c + 1}): '))

soma = somacol = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end = ' ')
        if m[l][c] % 2 == 0:
            soma += m[l][c]
        if c == 2:
            somacol += m[l][c]
        if l == 1:
            maior = m[1][0]
        else:
            if m[1][c] > maior:
                maior = m[1][c]
    print()

print(f'\nA soma dos números pares da matriz é {soma}.\nA soma dos números da terceira coluna é {somacol} e o maior número da segunda linha é {maior}')