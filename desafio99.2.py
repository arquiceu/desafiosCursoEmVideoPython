#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 99 - Curso de Python do canal Curso em video
# https://youtu.be/vp9UX7wr92o
# Versão com parâmetro variável na função maior()


from time import sleep


def maior(*n):
    print('-=' * 15)
    print('Analisando os valores passados...')
    quant_numeros = 0
    numero_maior = 0
    for v in n:
        sleep(.5)
        print(f'{v}', end=' ', flush=True)
        if quant_numeros == 0:
            numero_maior = v
        else:
            if v > numero_maior:
                numero_maior = v
        quant_numeros += 1
    sleep(.5)
    if quant_numeros == 0:
        print(f'Nenhum número foi informado.\n')
        sleep(1)
    else:
        print(f'\nForam informados {quant_numeros} números, e destes, o maior é {numero_maior}\n')
        sleep(1)


maior(23, 56, 12, 8, 0, 2, 5, 43)
maior()
maior(32, 29, 14)
maior(3, 4, 5)
maior(12, 24, 36, 48)
