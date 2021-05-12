print('=' * 40, end = '\n')
print(f'{"PROGRAMA DE VERIFICAÇÃO DE PESOS":^40}')
print('=' * 40, end = '\n\n')

l = []
j = []

maior = menor = 0

while True:
    l.append(str(input('Nome: ')))
    l.append(float(input('Peso: ')))

    if len(j) == 0:
        maior = menor = l[1]
    else:
        if l[1] > maior:
            maior = l[1]
        if l[1] < menor:
            menor = l[1]
    
    j.append(l[:])
    l.clear()

    key = str(input('Quer continuar? [s / n] ')).lower().strip()
    if key != 's':
        break

print('-' * 40, end = '\n')
print(f'{"TOTAL DE PESSOAS CADASTRADAS: ":^36}{len(j):^4}')

print(f'\nO maior peso registrado foi {maior}, dos indivíduos: ')

for p in j:
    if p[1] == maior:
        print(f'{p[0]}', end = ', ')

print(f'\nO menor peso registrado foi {menor}, dos indivíduos: ')

for p in j:
    if p[1] == menor:
        print(f'{p[0]}', end = ', ')