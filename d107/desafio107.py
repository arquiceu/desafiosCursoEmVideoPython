#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 107 do curso de Python do canal Curso em Video
# https://youtu.be/y8pI8YBphQI
# Módulo __main__


if __name__ == '__main__':
    import moeda
    preco = float(input('Digite o preço: R$ '))
    print(f'A metade de R$ {preco:.2f} é R$ {moeda.metade(preco):.2f}')
    print(f'O dobro de R$ {preco:.2f} é R$ {moeda.dobro(preco):.2f}')
    print(f'Diminuindo 10% de R$ {preco:.2f}, temos R$ {moeda.diminuir(preco, 10):.2f}')
    print(f'Aumentando 10% de R$ {preco:.2f}, temos R$ {moeda.aumentar(preco, 10):.2f}')
