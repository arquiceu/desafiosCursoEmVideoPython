#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 101 do Curso de Python do canal Curso em Vídeo
# https://youtu.be/czDcimdc3GU


def voto(ano_nascimento=0):
    '''    
    Print a condicao de eleitor conforme a data de nascimento
    ano_nascimento: numero int, default is zero
    '''
    from datetime import date
    ano_atual = date.today().year
    try:
        idade = ano_atual - ano_nascimento
    except(TypeError, ValueError):
        print('ERRO! Digite um número válido para ano de nascimento!')
    if type(ano_nascimento) is int:
        if idade < 0:
            return 'ERRO! Digite um número válido para ano de nascimento!'
        if idade > 0 and idade < 16:
            return f'Com {idade} ano(s) NÃO VOTA!'
        elif idade == 0:
            return f'Com menos de 1 ano NÃO VOTA!'
        elif (idade >= 16 and idade < 18) or idade >= 65:
            return f'Com {idade} anos o VOTO É OPCIONAL!'
        elif idade >=18 and idade < 65:
            return f'Com {idade} anos o VOTO É OBRIGATÓRIO!'


print(voto(int(input('Em que ano você nasceu? '))))
