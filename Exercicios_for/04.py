'''Escreva um programa que solicite do usuário dois valores positivos e imprima
todos os números inteiros dentro desse intervalo excluindo-se o valor inicial do
intervalo e o valor final. Ao término, informe que o programa foi encerrado.'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

for i in range(n1 + 1, n2):
    print(i)