#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 112 do curso de Python do canal Curso em Video
# https://youtu.be/6vADeY5_pMs
# Modulo dado

def leiadinheiro(texto='Digite o valor: '):
    def mensagemerro(erro='vazio'):
        if erro == 'vazio':
            print('Digite um valor válido!')
        if erro == 'nan':
            print(f'\"{x}\" não é um valor válido!')
    while True:
        x = str(input(texto)).strip()
        if len(x) == 0:
            mensagemerro()
        else:
            c = 0
            if x.count(',') > 0:
                x = x.replace(',', '.')
            while True:
                try:
                    x = float(x)
                    c = 1
                    break
                except:
                    mensagemerro('nan')
                    break
            if c == 1:
                break
    return x
