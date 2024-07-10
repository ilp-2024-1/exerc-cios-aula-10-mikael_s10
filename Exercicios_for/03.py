'''Escreva um programa que solicite do usuário dois valores positivos
e imprima todos os números inteiros dentro desse intervalo. O
algoritmo deve armazenar cada valor em duas variáveis diferentes
(v_ini e v_fim). Ao término, informe que o programa foi encerrado.'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

for i in range(n1 + 1, n2 ):
    v_ini = i
    print(v_ini)
    v_fim = i

