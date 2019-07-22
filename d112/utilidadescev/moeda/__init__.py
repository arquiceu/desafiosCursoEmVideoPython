#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 112 do curso de Python do canal Curso em Video
# https://youtu.be/6vADeY5_pMs
# Modulo moeda


def moeda(x=0, y='R$'):
    if y == 'R$':
        return f'{y:>4}{x:>15.2f}'.replace('.',',')


def aumentar(x, y=0, m=False):
    z = x + ((x / 100) * y)
    return z if m == False else moeda(z, m)


def diminuir(x=0, y=0, m=False):
    z = x - ((x / 100) * y)
    return z if m == False else moeda(z, m)


def dobro(x=0, m=False):
    z = x * 2
    return z if m == False else moeda(z, m)


def metade(x=0, m=False):
    z = x / 2
    return z if m == False else moeda(z,m)


def resumo(x=0, y=0, z=0, m=False):
    if m == False:
        res = f'''
        {"-" * 40}
        {"RESUMO DO VALOR":^40} 
        {"-" * 40}
        Preço analisado: {x}
        Dobro do preço: {dobro(x)}
        Metade do preço: {metade(x)}
        Com {y}% de aumento: {aumentar(x, y)}
        Com {z}% de redução: {diminuir(x, z)}
        '''
        return res
    else:
        res = f'''
        {"-" * 40}
        {"RESUMO DO VALOR":^40} 
        {"-" * 40}
        {"Preço analisado:":<20}{moeda(x)}
        {"Dobro do preço:":<20}{dobro(x, m)}
        {"Metade do preço:":<20}{metade(x, m)}
        {f"Com {y}% de aumento:":<20}{aumentar(x, y, m)}
        {f"Com {z}% de redução:":<20}{diminuir(x, z, m)}
        '''
        return res
 