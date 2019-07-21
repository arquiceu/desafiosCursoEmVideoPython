#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 107 do curso de Python do canal Curso em Video
# https://youtu.be/y8pI8YBphQI


def aumentar(x, y=10):
    z = x + ((x / 100) * y)
    return z
    
    
def diminuir(x, y=10):
    z = x - ((x / 100) * y)
    return z
    
    
def dobro(x):
    z = x * 2
    return z

    
def metade(x):
    z = x / 2
    return z
