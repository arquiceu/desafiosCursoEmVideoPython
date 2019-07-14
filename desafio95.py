#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 95 - Curso de Python do Canal Curso em Vídeo
# https://www.youtube.com/watch?v=mw1So0r317Y&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=29

jogadores = list()
continuar = True


while continuar == True:
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
                gols_por_partida.append(int(input(f'    Quantos gols na partida {i}? ')))
                break
            except(TypeError, ValueError):
                print('Você deve digitar um número inteiro.')
    jogador = dict()
    jogador['nome'] = nome
    jogador['gols'] = gols_por_partida.copy()
    del gols_por_partida
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    del jogador
    continua = None
    while True:
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
        if continua not in 'SN':
            print('Digite apenas "S" para sim ou "N" ou para não.')
        else:
            if continua == 'S':
                break
            elif continua == 'N':
                continuar = False
                break
            else:
                print('Digite apenas "S" para sim ou "N" ou para não.')
else:
    print('-=' * 30)
    print(f'    {"Nº":<3}{"Nome":<15}{"Gols":<25}{"Total de gols":<13}')
    print('-' * 60)
    for k, v in enumerate(jogadores):
        print(f'    {k + 1:<3}{str(v.get("nome")):<15}{str(v.get("gols")):<25}{str(v.get("total")):<13}')
    print('-' * 60)
    while True:
        levantamento = input('Mostrar dados de qual jogador? (999 para sair) ')
        if levantamento == '999':
            print('-' * 60)
            print('  <<ENCERRADO>>')
            break
        try:
            levantamento2 = int(levantamento)
            if levantamento2 - 1 in list(range(len(jogadores))):
                print('-' * 60)
                print(f' --- LEVANTAMENTO DO JOGADOR {jogadores[levantamento2 - 1]["nome"]}')
                for k, v in enumerate(jogadores[levantamento2 - 1]['gols']):
                    print(f'     No jogo {k + 1} fez {v} gol(s)')
                del(levantamento2)
            else:
                print('-' * 60)
                print(f'ERRO! Não existe jogador com código {levantamento2}. Escolha entre: 1 até {len(jogadores)}.')
                del(levantamento2)
        except:
            print('-' * 60)
            print(f'Digite somente um dos NÚMEROS da lista. Escolha entre: 1 até {len(jogadores)}.')
