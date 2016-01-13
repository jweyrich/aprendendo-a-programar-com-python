#!/usr/bin/env python3

from datetime import date

def data_por_extenso(data):
	mes_por_extenso = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
	(dia, mes, ano) = data.day, data.month, data.year
	return '%s de %s de %s' % (dia, mes_por_extenso[int(mes) - 1], ano)

data = date.today()
resultado = data_por_extenso(data)
print(resultado)
