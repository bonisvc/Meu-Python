l = []

while True:
    try:
        x = int(input('Digite um valor (ou digite 999 para encerrar): '))
        if x == 999:
            break
        if l.count(x) > 0:
            print('Valor duplicado, será desconsiderado...')
        else:
            l.append(x)
    except:
        ValueError()

print(sorted(l))

#print(set(l))