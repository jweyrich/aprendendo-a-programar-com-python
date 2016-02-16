#!/usr/bin/env python3

# Lâ as notas
notas = []
for x in range(1,4):
	nota = input('Nota {}: '.format(x))
	nota = float(nota)
	if (nota > 10.0 or nota < 0.0):
		print('Nota inválida!')
		import sys; sys.exit() # Aborta o programa!
	notas.append(nota)

# Calcula a média
mediaCalculada = ( notas[0] + (notas[1] * 2) + (notas[2] * 3) ) / 6.0

# Imprime as notas
print("--------------- Notas ---------------")
for x in range(1,4):
	print('Nota {}:'.format(x), notas[x-1])
print('Média:', mediaCalculada)

print("-------------- Conceito -------------")
# Imprime o conceito
if mediaCalculada >= 9.0:
	print('A - APROVADO')
elif mediaCalculada >= 7.5:
	print('B - APROVADO')
elif mediaCalculada >= 6.0:
	print('C - APROVADO')
elif mediaCalculada >= 4.0:
	print('D - REPROVADO')
else:
	print('E - REPROVADO')
