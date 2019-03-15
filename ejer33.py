#-*-coding:utf-8-*-

'''Leer un número entero y 
determinar si termina en 7.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero % 10 == 7:
		print "El numero ingresado termina en 7"

	else:
		print "El numero ingresado no termina en 7"

except ValueError:
	print "El numero digitado debe ser un valor numerico"