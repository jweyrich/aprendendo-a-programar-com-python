#!/usr/bin/env python3

import random

numTentativas = 0

numero = random.randint(1, 20)
print('Estou pensando em um numero entre 1 e 20.')

while numTentativas < 5:
	numeroUsuario = input('Adivinhe: ')
	numeroUsuario = int(numeroUsuario)

	numTentativas = numTentativas + 1

	if numeroUsuario < numero:
		print('Tente mais alto.')

	if numeroUsuario > numero:
		print('Tente mais baixo.')

	if numeroUsuario == numero:
		break

if numeroUsuario == numero:
	print('Muito bem! Voce acertou o numero em ' + str(numTentativas) + ' tentativas!')

if numeroUsuario != numero:
	numero = str(numero)
	print('Errado. O número era ' + numero)

