#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 93 - Curso de Python do Canal Curso em Vídeo
# https://youtu.be/5yKiud-YNaE


jogador = dict()
nome = str(input('Digite o nome do jogador: ')).strip()
while True:
    try:
        quantidade_partidas = int(input(f'Quantas partidas {nome} jogou? '))
        break
    except(TypeError, ValueError):
        print('Você deve digitar um número inteiro.')
gols_por_partida = list()
for i in range(1, quantidade_partidas + 1):
    while True:
        try:
            gols_por_partida.append(int(input(f'Quantos gols na partida {i}? ')))
            break
        except(TypeError, ValueError):
            print('Você deve digitar um número inteiro.')
jogador['nome'] = nome
jogador['gols'] = gols_por_partida
jogador['total'] = sum(gols_por_partida)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('-=' * 30)
print(f'O jogador {nome} jogou {quantidade_partidas} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'    => Na partida {k + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
