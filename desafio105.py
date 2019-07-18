#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 105 do curso de Python do canal Curso em Vídeo
# https://youtu.be/Kbs97l38vVQ


def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações com sobre a situação da turma
    '''
    dbnotas = dict()
    dbnotas['total'] = sum(n)
    dbnotas['maior'] = max(n)
    dbnotas['menor'] = min(n)
    dbnotas['media'] = sum(n) / len(n)
    if sit:
        if dbnotas['media'] < 5 and dbnotas['media'] >= 0:
            situacao = 'INSUFICIENTE'
        elif dbnotas['media'] >= 5 and dbnotas['media'] < 6:
            situacao = 'REGULAR'
        elif dbnotas['media'] >= 6 and dbnotas['media'] < 8:
            situacao = 'ADEQUADO'
        elif dbnotas['media'] >= 8 and dbnotas['media'] <= 10:
            situacao = 'DESEJAVEL'
        elif  dbnotas['media'] > 10 and dbnotas['media'] < 0:
            situacao = 'ALGO ERRADO NAO ESTA CERTO KK'
        dbnotas['situacao'] = situacao
    return dbnotas


resp = notas(2.3, 4.5, 10)
print(resp)
help(notas)
