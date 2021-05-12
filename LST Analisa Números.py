l = []

cont = 0

while True:
    try:
        n = int(input('Digite um número maior que zero(ou digite 0 para encerrar): '))
        if n == 0:
            break
        l.append(n)
        cont += 1
    except:
        ValueError()

sorted(l)

if l.count(5) > 0:
    print(f'Foram digitados {cont} números, com o número 5 sendo digitado {l.count(5)} vezes e a lista em ordem decrescente: {sorted(l, reverse = True)}')
else:
    print(f'Foram digitados {cont} números, não houve nenhum número 5 digitado e a lista em ordem decrescente: {sorted(l, reverse = True)}')