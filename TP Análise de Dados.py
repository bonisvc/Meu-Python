print('\n', '-' * 50, '\n')

n = (int(input('Digite um número inteiro: ')), int(input('Digite um número inteiro: ')), 
    int(input('Digite um número inteiro: ')), int(input('Digite um número inteiro ')))

print(f'Você digitou os números: {n}')

if n.count(9) > 0:
    print(f'\nExistem {n.count(9)} números 9 entre os números digitados.')
else:
    print('\nVocê não digitou nenhum número 9')
try:
    print(f'\nO número 3 está na {n.index(3) + 1}° posição.')
except:
    print('\nVocê não digitou nenhum número 3.')

print('\nOs números pares são:', end = ' ')

for c in n:
    if c % 2 == 0:
        print(c, end = ' ')

print('\n', '-' * 50)