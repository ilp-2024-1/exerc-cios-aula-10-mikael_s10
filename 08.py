'''Escreva um programa que peça ao usuário para digitar um número inteiro e,
em seguida, calcule a soma dos dígitos desse número usando um loop while.
Ao término, informe que o programa foi encerrado.
Ex: entrada: 19.623 à saída: 21; entrada: 456 à saída: 15;'''

n1 = input('Digite um valor: ')

while True:
    lista = [int(digito) for digito in n1]
    break
print(sum(lista))