'''l = []

n = str(input('Digite uma expressão matemática: '))
l.extend(n)

if l.count('(') == l.count(')'):
    print('A expressão está correta.')
else:
    print('A expressão está errada.')'''

exp = str(input('Digite uma expressão matemática: '))

pilha = []

for x in exp:
    if x == '(':
        pilha.append('(')
    elif x == ')':
        if len(pilha) > 0:
            pilha.pop
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')