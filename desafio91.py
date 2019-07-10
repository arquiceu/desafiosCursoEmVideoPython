#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=cwrqIztaAwk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=25


from random import randint
from time import sleep
from operator import itemgetter


while True:
    try:
        quantidade_de_jogadores = int(input('Quantos jogadores participarão? '))
        break
    except:
        print('Digite um número inteiro.')
jogadores = dict()
ranking = None


print('Números Sorteados:')
sleep(1)
for i in range(1, quantidade_de_jogadores + 1):
    jogadores[f'Jogador{i}'] = randint(1, 6)
    print(f'{f"Jogador{i}"} tirou {jogadores[f"Jogador{i}"]} no dado.')
    sleep(1)


print('-=' * 30)
print(f'{"== RANKING DOS JOGADORES ==":^60}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    text = f'{k + 1}º lugar: {v[0]} com {v[1]}'
    print(f'{text:^60}')
    sleep(1)
