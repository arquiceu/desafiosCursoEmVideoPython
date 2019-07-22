#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Resposta ao desafio 112 do curso de Python do canal Curso em Video
# https://youtu.be/6vADeY5_pMs
# Módulo __main__


if __name__ == '__main__':
    from utilidadescev import moeda, dado
    preco = dado.leiadinheiro('Digite o preço: R$ ')
    print(moeda.resumo(preco, 10, 20, 'R$'))
