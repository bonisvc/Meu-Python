lista = []

for l in range(0, 5):
    x = int(input(f'Digite o {l + 1}° valor: '))
    if l == 0 or x > lista[-1]:
        lista.append(x)
        print(f'O valor {x} foi adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                print(f'O valor {x} foi inserido na posição {pos} da lista.')
                break
            pos += 1

print(lista)
print('Fim da aplicação')
                
