tupla = ('Caderno', 12.00, 'Lapiseira', 6.90, 'Borracha', 1.50, 
        'Pasta', 3.20, 'Caneta', 1.50, 'Marca Texto', 3.80, 
        'Corretor Líquido', 5.60, 'Mochila', 98.50, 'Papel A4', 9.80)

print('\n\n', '-'* 39, '\n', '{:^39}'.format('Lista de Preços'), '\n', '-' * 39, '\n\n')

for c in range(0, len(tupla) // 2):
    inicio = c * 2
    print(f'{tupla[inicio]:.<32}', f'R$ {tupla[inicio + 1]:>5.2f}')

print('\n\n', '-' * 39)