a = b = c = d = e = 0

argumentos = [a, b, c, d, e]

for x in range (0, len(argumentos)):
    try:
        y = int(input('Digite um número: '))
        argumentos[x] = y
    except:
        ValueError()
print(f'Os números digitados em ordem crescente foram: {sorted(argumentos)}')

