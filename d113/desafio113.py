#!/usr/bin/env python
# -*- coding: utf-8 -*-


from validadornum import validadorint
from validadornum import validadorfloat


while not validadorint(numero := input('Digite um número inteiro: ')):
        continue

while not validadorfloat(numero := input('Digite um número float: ')):
        continue
