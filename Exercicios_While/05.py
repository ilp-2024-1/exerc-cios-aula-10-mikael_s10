'''Escreva um programa que solicita ao usuário um valore numérico inteiro positivo e, em
seguida, calcule o fatorial desse número usando um loop do tipo while. Ao final o
programa deverá exibir o valor do fatorial do número informado pelo usuário e término
do programa.'''

n1 = int(input('Digite um numero inteiro positivo: '))
fatorial = 1
while (n1 > 1):
    fatorial = fatorial * n1
    n1 -= 1
    print(fatorial)
    
print('fim')