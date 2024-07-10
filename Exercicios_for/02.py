'''Escreva um programa que solicite do usuário um valor positivo e
imprima todos os números inteiros de 1 até o número digitado pelo
usuário. Ao término, informe que o programa foi encerrado.'''

n = int(input('Digite um valor: '))

for i in range(1, n + 1):
    print(i)