#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 98 - Curso de Python do canal Curso em Video
# https://youtu.be/DCBlt_z2UOE


from time import sleep


def contador(de, ate, passo):
    print('-=' * 15)
    print(f'Contagem de {de} ate {ate} de {abs(passo)} em {abs(passo)}')
    if de < ate:
        for i in range(de, ate + 1, passo):
            print(i, end=' ', flush= True)
            sleep(.5)
        print('FIM!')
    elif de > ate:
        for i in range(de, ate - 1, -abs(passo)):
            print(i, end=' ', flush = True)
            sleep(.5)
        print('FIM!')
    print('\n')



contador(1, 10, 1)
contador(10, 0, 2)


print('Agora e sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

