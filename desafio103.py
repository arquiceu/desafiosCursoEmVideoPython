#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 103 do curso de Python do canal Curso em Vídeo
# https://youtu.be/FbOvilKfHMI


def ficha(nome='<desconhecido>', gols=0):
    '''
    -> Mostra frase indicando quantos gols o jogador fez.
    :param nome: string, nome do jogador
    :param gols: int, numero de gols
    :return: frase com nome do jogador e quantidade de gols
    '''
    nome2 = nome
    gols2 = gols
    nome3 = str(input('Nome do Jogador: ')).strip().upper()
    if nome3 != '':
        nome = nome3
    else:
        nome = nome2
    try:
        gols3 = int(input('Número de gols: '))
        gols = gols3
    except(TypeError, ValueError):
        gols = gols2
    return f'O jogador {nome} fez {gols} gols no campeonato.'


print(ficha())
help(ficha)
