#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 102 do Curso de Python do canal Curso em Vídeo
# https://youtu.be/84jUX96cs7Q


def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (opcional) mostra ou nao a conta
    :return: O valor do fatorial de um numero n
    '''
    c = 1
    s = ''
    if show:
        for i in range(n, 0, -1):
            if i != 1:
                s += f'{i} * '
            else:
                s += f'{i} = {c}'
                break
            c *= i
        return s
    else:
        for i in range(n, 0, -1):
            c *= i
        return c


print(fatorial(10))
