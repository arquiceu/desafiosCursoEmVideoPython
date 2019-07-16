#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 98 - Curso de Python do canal Curso em Video
# https://youtu.be/DCBlt_z2UOE


from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 15)
    if inicio == fim:
        passo = 1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} ate {fim} de {abs(passo)} em {abs(passo)}')
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush= True)
            sleep(.5)
        print('FIM!')
    elif inicio > fim:
        for i in range(inicio, fim - 1, -abs(passo)):
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
