x = int(input('Quantos números deseja inserir na sua lista? '))

soma = par = impar = maior = menor = 0

n = []

for lista in range (0, x):
    y = int(input(f'Digite o {lista + 1}° número: '))
    n.append(y)
    soma += y
    if lista == 1:
        maior = y
        menor = y
    if y > maior:
        maior = y
    if y < menor:
        menor = y
    if y % 2 == 0:
        par += 1
    if y % 2 != 0:
        impar += 1

print(f'\nVocê digitou {x} números, que são: {n}\n\nA soma entre eles é {soma} e a média aritmética é {soma / x}\nO maior número digitado é {maior}\nO menor número digitado é {menor}\n\nVocê digitou {par} números pares e {impar} números ímpares.')
    
    