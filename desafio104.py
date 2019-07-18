#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 104 do curso de Python do canal Curso em Vídeo
# https://youtu.be/VrQmMbPpbf0


def leiaint():
    '''
    -> Capta número inteiro inputado por usuário
    :return: número inteiro
    '''
    numero = None
    while True:
        try:
            numero = int(input('Digite um número: '))
            break
        except(TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido.')
    return numero


a = leiaint()
print(f'Você acabou de digitar o número {a}.')
