#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 109 do curso de Python do canal Curso em Video
# https://youtu.be/Y0zNYTHoGhQ

def moeda(x=0, y='R$'):
    if y == 'R$':
        return f'{y}{x:>8.2f}'.replace('.',',')


def aumentar(x, y=10, m=False):
    z = x + ((x / 100) * y)
    return z if m == False else moeda(z, m)


def diminuir(x=0, y=10, m=False):
    z = x - ((x / 100) * y)
    return z if m == False else moeda(z, m)


def dobro(x=0, m=False):
    z = x * 2
    return z if m == False else moeda(z, m)


def metade(x=0, m=False):
    z = x / 2
    return z if m == False else moeda(z,m)
