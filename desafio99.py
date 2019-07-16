#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 99 - Curso de Python do canal Curso em video
# https://youtu.be/vp9UX7wr92o
# Versão com lista no parâmetro da função maior()


from random import randint
from time import sleep


minimo_de_numeros_que_podem_ser_escolhidos = 0
maximo_de_numeros_que_podem_ser_escolhidos = 10
menor_numero_que_pode_ser_escolhido = -100
maior_numero_que_pode_ser_escolhido = 100


def numeros():
    return [randint(menor_numero_que_pode_ser_escolhido, maior_numero_que_pode_ser_escolhido) for i in range(minimo_de_numeros_que_podem_ser_escolhidos, randint(0,maximo_de_numeros_que_podem_ser_escolhidos))]


def maior(n):
    print('-=' * 15)
    print('Analisando os valores passados...')
    sleep(.5)
    if len(n) == 0:
        print(f'Nenhum número foi informado.\n')
        sleep(1)
    else:
        for k, v in enumerate(n):
            sleep(.5)
            print(v, end=' ', flush= True)
        sleep(.5)
        print(f'\nForam informados {len(n)} números, e destes, o maior é {max(n)}\n')
        sleep(1)
    

maior(numeros())
maior(numeros())
maior(numeros())
maior(numeros())
maior(numeros())
