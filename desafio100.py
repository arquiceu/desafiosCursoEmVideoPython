#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 100 - Curso de Python do canal Curso em video
# https://youtu.be/MEs-41JcuhM


from random import randint
from time import sleep


minimo_de_numeros_que_podem_ser_sorteados = 0
maximo_de_numeros_que_podem_ser_sorteados = 10
menor_numero_que_pode_ser_sorteado = -100
maior_numero_que_pode_ser_sorteado = 100


def numeros():
    numeros_sortedos = [randint(menor_numero_que_pode_ser_sorteado, maior_numero_que_pode_ser_sorteado) for i in range(minimo_de_numeros_que_podem_ser_sorteados, randint(0,maximo_de_numeros_que_podem_ser_sorteados))]
    print(f'Sorteando {len(numeros_sortedos)} valores da lista: ', end='')
    for i in numeros_sortedos:
        sleep(.5)
        print(f'{i}', end=' ', flush = True)
    sleep(.5)
    print('PRONTO!')
    return numeros_sortedos


def somapares(n):
    sleep(.5)
    print(f'Somando o números pares de {n}, temos ', end='')
    sleep(.5)
    somapares = 0
    for i in n:
        if i % 2 == 0:
            somapares += i
    sleep(.5)
    print(f'{somapares}')
    

somapares(numeros())
