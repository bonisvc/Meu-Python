print('_'*50, end = '\n\n')
print('{:^50}'.format('SERVIÇO DE CADASTRAMENTO SOCIAL'))
print('_'*50, end = '\n\n')

pessoa = []
lista = []
cont = 0

while True:
    nome = str(input('Digite o nome da pessoa: ')).upper().strip()
    sexo = str(input('Qual o sexo biológico da pessoa? (h - homem/m - mulher) ')).upper().strip()
    
    if sexo == 'H':
        x = 'o'
        s = 'HOMEM'
    else:
        x = 'a'
        s = 'MULHER'
    
    idade = int(input(f'Qual a idade d{x} {nome}? '))
    civil = str(input(f'Qual o estado civil d{x} {nome}? (c = casad{x}/s = solteir{x}) ')).upper().strip()
    
    if civil == 'C':
        c = f'CASAD{x.upper()}'
    else:
        c = f'SOLTEIR{x.upper()}'


    pessoa = [nome, s, idade, c]
    lista.append(pessoa[:])
    
    cont += 1
    
    ver = str(input('\n\nDeseja cadastrar uma nova pessoa? (s - sim/n - não) ')).upper().strip()
    if ver == 'N':
        break

print(f'\n\nForam inseridos os dados de {cont} pessoas:\n')
print(f'{"NOME":^12} {"SEXO":^6} {"IDADE":^7} {"SITUAÇÃO":^10}')

for d in lista:
    print(f'{d[0]} {"."*(12-len(d[0]))} {d[1]:^6} {d[2]:^2} anos {d[3]:^10}')

print('\n\n', '_'*50, end = '\n\n')