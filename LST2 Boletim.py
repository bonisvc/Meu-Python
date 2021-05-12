from time import sleep

l = []
aluno = []
nota = []
cont = 0

while True:
    aluno.append(str(input('Nome do Aluno: ')))
    nota.append(float(input('Nota da AV1: ')))
    nota.append(float(input('Nota da AV2: ')))
    
    aluno.append(nota[:])
    nota.clear()

    l.append(aluno[:])
    aluno.clear()

    verifica = str(input('Cadastrar novo aluno? (s/n)')).lower().strip()
    if verifica != 's':
        print('\n\nProcessando. . .')
        sleep(3)

        print(f'\n\n{"ID":^4}{"NOME":^12}{"MÉDIA":>}')
        print(f'{"_"*21:^21}')

        for c in l:
            média = (c[1][0] + c[1][1]) / 2
            
            print(f'{cont + 1:^4}{c[0]:<12}{média:>.2f}')
            cont += 1
        
        print(f'{"_"*21:^21}')

        verifica = int(input('\nDeseja visualizar as notas de qual aluno? (0 para encerrar): '))

        if verifica > 0 and verifica <= cont:
            print(f'\nAs notas de {l[verifica - 1][0]} são: AV1 {l[verifica - 1][1][0]} e AV2 {l[verifica - 1][1][1]}')
            print('\n\nAplicação encerrada.')
        else:
            print('\n\nAplicação encerrada.')
        
        break