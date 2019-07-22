#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 110 do curso de Python do canal Curso em Video
# https://youtu.be/1Ks218WINT8
# Módulo __main__


if __name__ == '__main__':
    from moeda import moeda, metade, dobro, aumentar, diminuir, resumo
    preco = float(input('Digite o preço: R$ '))
    print(resumo(preco, 10, 20, 'R$'))
