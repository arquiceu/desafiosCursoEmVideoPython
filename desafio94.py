#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desafio 94 - Curso de Python do canal Curso em Vídeo
# https://youtu.be/ETnExBCFeps


pessoas = list()
pessoa = dict()
sair = False
soma_todas_idades = 0
media_idades = None
quantidade_de_mulheres = 0


while sair == False:
    pessoa['nome'] = str(input('Nome: ')).strip()
    
    while True:
        sexo = str(input('Sexo: [M/F]')).strip().upper()
        if sexo not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            if sexo == 'M':
                pessoa['sexo'] = sexo
                break
            elif sexo == 'F':
                pessoa['sexo'] = sexo
                break
            else:
                print('ERRO! Por favor, digite apenas M ou F.')
    
    while True:
        try:
            pessoa['idade'] = int(input('Idade: '))
            break
        except(TypeError, ValueError):
            print('ERRO! Por favor, digite um número inteiro.')
    
    pessoas.append(pessoa.copy())
    pessoa.clear()
    
    while True:
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
        if continuar not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
        else:
            if continuar == 'N':
                sair = True
                break
            elif continuar == 'S':
                break
            else:
                print('ERRO! Por favor, digite apenas S ou N.')


print('-=' * 30)


print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')


for i in range(0, len(pessoas)):
    soma_todas_idades += pessoas[i]['idade']
media_idades = soma_todas_idades / len(pessoas)
print(f'B) A média de idade é {media_idades:.0f} anos.')
for i in range(0, len(pessoas)):
    if pessoas[i]['sexo'] == 'F':
        quantidade_de_mulheres += 1


print(f'C) As {quantidade_de_mulheres} mulheres cadastradas foram:', end=' ')
a = quantidade_de_mulheres
for i in range(0, len(pessoas)):
    if pessoas[i]['sexo'] == 'F' and a > 2:
        print(f'{pessoas[i]["nome"]}', end=', ')
        a -= 1
    elif pessoas[i]['sexo'] == 'F' and a == 2:
        print(f'{pessoas[i]["nome"]}', end=' ')
        a -= 1
    elif pessoas[i]['sexo'] == 'F' and a == 1:
        print(f'e {pessoas[i]["nome"]}', end='.')
        a -= 1
        break


print(f'\nD) Lista das pessoas que estão acima da média: ')
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media_idades:
        print(f'    nome = {pessoas[i]["nome"]}; sexo = {pessoas[i]["sexo"]}; idade = {pessoas[i]["idade"]};')


print('\n<< ENCERRADO >>')
