#!/usr/bin/env python3

texto = 'INICIAL'

def funcao():
	global texto
	texto = 'MUDOU'
	
funcao()
print(texto)
