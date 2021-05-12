matriz = []
linha = []
maior = menor = somal = somac = soma = 0

for l in range(0, 3):

    for c in range(0, 3):
        linha.append(int(input(f'Digite o elemento [{l + 1}, {c + 1}] da matriz: ')))

    matriz.append(linha[:])
    linha.clear()

for g in range(0, 3):

    for h in range(0, 3):
        print(f'[{matriz[g][h]}]', end = ' ')
        soma += matriz[g][h]
    
    print()

print(f'A soma dos valores digitados é: {soma}')

while True:

    v = str(input('Deseja somar uma linha ou uma coluna (digite 0 para encerrar):\nL = Linha \nC = Coluna ')).lower().strip()
    print()

    if v == '0':
        break
    
    if v == 'l':
        qlinha = int(input('Qual a linha que deseja somar? '))

        for sl in range(0, 3):
            somal += matriz[qlinha - 1][sl]
        
        print(f'A soma da linha {qlinha} é: {somal}')

    if v == 'c':
        qcoluna = int(input('Qual a coluna que deseja somar? '))

        for cl in range(0, 3):
            somac += matriz[cl][qcoluna - 1]

        print(F'A soma da coluna {qcoluna} é: {somac}')
    
    verifica = str(input('Deseja realizar uma nova verificação? (s/n) ')).lower().strip()
    
    if verifica != 's':
        break