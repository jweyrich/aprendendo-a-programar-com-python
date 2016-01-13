#!/usr/bin/env python3

string = input('Digite uma string: ')

def eh_minuscula1(original):
	''' Permite somente letras minúsculas (inclusive com acentuação). '''
	for c in original:
		if not c.islower():
			return False
	return True

def eh_minuscula2(original):
	''' Permite letras minúsculas (inclusive com acentuação), pontuação, números, etc. '''
	convertida = string.lower()
	return original == convertida

def eh_minuscula3(original):
	''' Permite somente letras minúsculas (sem acentuação). '''
	import string
	for c in original:
		if c not in string.ascii_lowercase: # 'abcdefghijklmnopqrstuvwxyz' # not locale-dependent
			return False
	return True

print('A string', 'é' if eh_minuscula1(string) else 'não é', 'toda minúscula')
