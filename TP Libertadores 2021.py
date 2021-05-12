a = 'Flamengo', 'LDU', 'Unión La Calera', 'Vélez'
b = 'Palmeiras', 'Defensa y Justicia', 'Independiente Del Vale', 'Universitario'
c = 'Fluminense', 'River Plate', 'Santa Fe', 'Junior'
d = 'Barcelona', 'Boca Juniors', 'Santos', 'The Strongest'

print(f'\nOs líderes de cada grupo são:\nGrupo A: {a[0]}\nGrupo B: {b[0]}\nGrupo C: {c[0]}\nGrupo D: {d[0]}')
print(f'\n\nOs últimos colocados de cada grupo são:\nGrupo A: {a[3]}\nGrupo B: {b[3]}\nGrupo C: {c[3]}\nGrupo D: {d[3]}')

libertadores = a + b + c + d
print(f'\nOs times participantes da Libertadores de 2021 são: {sorted(libertadores)}.')

busca = a.index('Flamengo')

print(f'O Flamengo está em {busca+1}° lugar do seu grupo.')