#!/usr/bin/env python3

val = 'INICIAL'

def funcao(arg):
	#print('DEBUG: arg ANTES =', id(arg))
	arg = 'MUDOU'
	#print('DEBUG: arg DEPOIS=', id(arg))

#print('DEBUG: val ANTES =', id(val))
funcao(val)
#print('DEBUG: val DEPOIS=', id(val))
print(val)

# str é imutável!