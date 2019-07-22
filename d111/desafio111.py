#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 111 do curso de Python do canal Curso em Video
# https://youtu.be/uBQ0--sRFUI
# Módulo __main__


if __name__ == '__main__':
    from utilidadescev import moeda
    preco = float(input('Digite o preço: R$ '))
    print(moeda.resumo(preco, 10, 20, 'R$'))
