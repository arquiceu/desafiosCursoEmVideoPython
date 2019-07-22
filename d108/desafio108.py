#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 107 do curso de Python do canal Curso em Video
# https://youtu.be/KtRkGEeUdqE
# Módulo __main__


if __name__ == '__main__':
    from moeda import moeda, metade, dobro, aumentar, diminuir
    preco = float(input('Digite o preço: R$ '))
    print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
    print(f'O dobro de R$ {moeda(preco)} é R$ {moeda(dobro(preco))}')
    print(f'Diminuindo 10% de R$ {moeda(preco)}, temos R$ {moeda(diminuir(preco, 10))}')
    print(f'Aumentando 10% de R$ {moeda(preco)}, temos R$ {moeda(aumentar(preco, 10))}')
