#-*-coding:utf-8-*-

'''Leer un numero entero y determinar si
es un numero terminado en 4.'''

try:
	numero = int(raw_input("Escribir el numero entero: "))

	entero = numero % 10

	if entero == 4:
		print "El numero digitado termina en 4"

	else:
		print "El numero digitado no termina en 4"

except ValueError:
	print "El numero digitado debe ser un valor numerico"