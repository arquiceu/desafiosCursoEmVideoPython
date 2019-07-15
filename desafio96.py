#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 96 - Curso de Python do Canal Curso em Vídeo
# https://youtu.be/oV1s53YGtvE


def area(dimensao1, dimensao2):
    print(f'A área de um terreno {dimensao1} x {dimensao2} é de {dimensao1 * dimensao2}m²')


print('Controle de Terrenos\n','-' * 20)
area(float(input('LARGURA (m): ')),float(input('COMPRIMENTO (m): ')))
