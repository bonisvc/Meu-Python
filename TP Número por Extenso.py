n = int(input('Digite um número entre 0 e 20: '))

while n not in range(0, 21):
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))

nome = ('um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

print(f'\n\nVocê digitou o número {nome[n-1]}.')