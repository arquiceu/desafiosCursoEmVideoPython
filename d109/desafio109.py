#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 109 do curso de Python do canal Curso em Video
# https://youtu.be/Y0zNYTHoGhQ
# Módulo __main__


if __name__ == '__main__':
    from moeda import moeda, metade, dobro, aumentar, diminuir
    preco = float(input('Digite o preço: R$ '))
    print(f'A metade de {moeda(preco, "R$")} é {metade(preco, "R$")}')
    print(f'O dobro de {moeda(preco, "R$")} é {dobro(preco, "R$")}')
    print(f'Diminuindo 10% de {moeda(preco, "R$")}, temos {diminuir(preco, 10, "R$")}')
    print(f'Aumentando 10% de {moeda(preco, "R$")}, temos {aumentar(preco, 10, "R$")}')
