palavras = 'amanha', 'hoje', 'talvez', 'amar', 'lua', 'abacate', 'otorrino', 'pato', 'acabou', 'fezinha', 'especial'

for c in palavras:
    print(f'\nNa palavra "{c}" existem as vogais: ', end = ' ')
    for vogal in c:
        if vogal.lower() in 'aeiou':
            print(vogal, end = ' ')

print('\n\n')