l = []
par = []
impar = []

for c in range(0, 7):
    
    l.append(int(input(f'Digite o {c + 1} número: ')))

for p in l:
    if p % 2 == 0:
        par.append(p)
    else:
        impar.append(p)

if len(par) > 0:
    print(sorted(par))
else:
    print('Você não digitou números pares.')
if len(impar) > 0:
    print(sorted(impar))
else:
    print('Você não digitou números ímpares.')