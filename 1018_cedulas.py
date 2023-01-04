# -*- codding utf-8 -*-

cedulas = [100, 50, 20, 10, 5, 2, 1]
qntCedulas = [0, 0, 0, 0, 0, 0, 0]

valor = int(input())
print(valor)

for i, c in enumerate(cedulas):
	qntCedulas[i] = int(valor/c)
	valor = valor%c

for i, q in enumerate(qntCedulas):
	print("{} nota(s) de R$ {},00".format(q, cedulas[i]))

