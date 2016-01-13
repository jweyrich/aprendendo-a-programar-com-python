#!/usr/bin/env python3

val = [1,2,3,4,5]

def funcao(arg):
	#print('DEBUG: arg ANTES =', id(arg))
	arg[0] = 99
	#print('DEBUG: arg DEPOIS=', id(arg))

#print('DEBUG: val ANTES =', id(val))
funcao(val)
#print('DEBUG: val DEPOIS=', id(val))
print(val)

# list é mutável!