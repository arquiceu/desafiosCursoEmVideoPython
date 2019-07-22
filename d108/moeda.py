#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 107 do curso de Python do canal Curso em Video
# https://youtu.be/KtRkGEeUdqE


def moeda(x=0, y='real'):
    if y == 'real':
        return f'{"R$"}{x:>8.2f}'.replace('.',',')


def aumentar(x, y=10):
    z = x + ((x / 100) * y)
    return z
    
    
def diminuir(x=0, y=10):
    z = x - ((x / 100) * y)
    return z
    
    
def dobro(x=0):
    z = x * 2
    return z

    
def metade(x=0):
    z = x / 2
    return z
