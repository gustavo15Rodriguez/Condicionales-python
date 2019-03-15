#-*-coding:utf-8-*-

'''Leer un número entero y 
determinar si es igual a 10.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero == 10:
		print "El numero ingresado es igual a 10"

	else:
		print "El numero ingresado no es igual a 10"

except ValueError:
	print "El numero digitado debe ser un valor numerico"