'''Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário
para adivinhar qual é o número. O programa deve continuar pedindo palpites até que
o usuário acerte o número. Ao final, o programa deve informar quantos palpites foram
necessários e informar que o programa encerrou.'''
import random



while True:
        sorteado = random.randint(0, 100)
        n1 = int(input('Digite um numero de 0 a 100: '))
        if sorteado != n1:
            print(F'tente denovo... O numero sorteado foi {sorteado}')
        else: 
            break
print('Parabens, vc acertou.')