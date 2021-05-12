l = []

while True:
    try:
        n = int(input('Digite um número: '))
        l.append(n)
        v = str(input('Deseja continuar? (s/n)')).upper().strip()
        if v == 'N':
            break
    except:
        ValueError()

lpar = []
limpar = []

for lista in l:
    if lista % 2 == 0:
        lpar.append(lista)
    else:
        limpar.append(lista)

print(sorted(lpar), sorted(limpar))
        
