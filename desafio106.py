#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 106 do curso de Python do canal Curso em Vídeo
# https://youtu.be/BMKYnZoxy88
# Não implementei cores porque no app de comandos do OS que uso não suporta


continuar = True


def pyhelp(comando=''):
    '''
    -> Função que invoca da função help() o docstring solicitado
    :param comando: recebe o nome da função ou bibliotéca da qual será mostrado o docstring
    '''
    if comando == '':
        print('Digite o nome de uma Função ou Bibliotéca.')
    elif str(comando).lower() == 'fim':
        global continuar
        continuar = False
        print('Até logo!')
    else:
        try:
            help(comando)
        except(NameError):
            print('Digite o nome de uma Função ou Bibliotéca.')


while True:
    print('SITEMA DE AJUDA PyHELP')
    c = str(input('Função ou Bibliotéca: ')).strip()
    pyhelp(c)
    if continuar == False:
        break
