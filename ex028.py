"""Escreva um programa que faça o computador "PENSAR", num número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu!
\
"""
from random import randint
from time import sleep  # Time e sleep faz uma contagem

computador = randint(0, 5)  # "RANDINT" Faz o computador "PENSAR" (Números aleatórios)
nome = str(input('Ola usuário está pronto?, para começar digite seu nome: '))
print('Certo, {} vamos ver se você é um jogador caro mesmo  hahahah'.format(nome))
sleep(1)
print('=-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-=' * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('\033[0:33mPROCESSANDO...\033[0:0m')
sleep(3)
if jogador == computador:
    print('\033[0:32mPARABÉNS {}! Você conseguiu me vencer!\033[0:0m'.format(nome))
else:
    print('\033[0:31m NÃO FOI DESSA VEZ, TENTE NOVAMENTE MAIS TARDE! {} e não no {}!\033[0:0m'.format(computador,
                                                                                                      jogador))
