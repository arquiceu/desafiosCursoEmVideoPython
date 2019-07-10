#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 92 - Curso de Python do canal Curso em Vídeo
# https://www.youtube.com/watch?v=Vsqemzdrj78&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=26


from datetime import datetime


pessoas = dict()
status_carteira_de_trabalho = ano_nascimento = ano_de_contratacao = salario = numero_da_carteira_de_trabalho = None
idade_para_aposentar = ano_para_aposentar = None
anos_de_contribuicao_para_aposentar = 35


for i in range(1):
    nome_pessoa = str(input('Nome: ')).strip()
    while True:
        try:
            ano_nascimento = int(input('Ano de nascimento: '))
            break
        except(typeError, valueError):
            print('O ano deve ser um número inteiro.')
    while True:
        try:
            status_carteira_de_trabalho = int(input('Número da Carteira de Trabalho (digite 0 se não tem): '))
            break
        except(typeError, valueError):
            print('O número da carteira deve ser um número inteiro.')
    idade = datetime.now().year - ano_nascimento
    if status_carteira_de_trabalho != 0:
        numero_da_carteira_de_trabalho = status_carteira_de_trabalho
        status_carteira_de_trabalho = True
    else:
        status_carteira_de_trabalho = False
    if status_carteira_de_trabalho == False:
        pessoas[i + 1] = {'nome' : nome_pessoa, 'ano_nascimento' : ano_nascimento, 'idade' : idade, 'dados_trabalhistas' : {'status_carteira_de_trabalho' : status_carteira_de_trabalho}}
    else:
        while True:
            try:
                ano_de_contratacao = int(input('Ano de contratação: '))
                break
            except (typeError, valueError):
                print('O ano da contratação deve ser um número inteiro.')
        while True:
            try:
                salario = float(input('Salário: '))
                break
            except (typeError, valueError):
                print('Valor inválido para salário.')
        # idade_para_aposentar = (ano_de_contratacao + anos_de_contribuicao_para_aposentar) - ano_nascimento
        # ano_para_aposentar = ano_de_contratacao + anos_de_contribuicao_para_aposentar
        pessoas[i + 1] = {'nome' : nome_pessoa, 'ano_nascimento' : ano_nascimento, 'idade' : idade, 'dados_trabalhistas' : {'status_carteira_de_trabalho' : status_carteira_de_trabalho, 'numero_da_carteira_de_trabalho' : numero_da_carteira_de_trabalho, 'ano_de_contratacao' : ano_de_contratacao, 'salario' : salario, 'anos_de_contribuicao_para_aposentar' : anos_de_contribuicao_para_aposentar, 'ano_para_aposentar' : ano_de_contratacao + anos_de_contribuicao_para_aposentar,'idade_para_aposentar' : (ano_de_contratacao + anos_de_contribuicao_para_aposentar) - ano_nascimento}}


print('-=' * 30)
print(f'Nome: {pessoas[1]["nome"]}')
print(f'Idade: {pessoas[1]["idade"]}')
print(f'Nº da Carteira de Trabalho: {pessoas[1]["dados_trabalhistas"]["numero_da_carteira_de_trabalho"]}')
print(f'Ano de contratação: {pessoas[1]["dados_trabalhistas"]["ano_de_contratacao"]}')
print(f'Salário: {pessoas[1]["dados_trabalhistas"]["salario"]}')
print(f'Quantidade de anos contribuindo para a previdência: {pessoas[1]["dados_trabalhistas"]["anos_de_contribuicao_para_aposentar"]} anos')
print(f'Ano em que vai se aposentar: {pessoas[1]["dados_trabalhistas"]["ano_para_aposentar"]}')
print(f'idade em que vai se aposentar: {pessoas[1]["dados_trabalhistas"]["idade_para_aposentar"]} anos')
