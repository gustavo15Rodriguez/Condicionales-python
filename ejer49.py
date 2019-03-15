#-*-coding:utf-8-*-

'''Leer un número entero y si es múltiplo de 4 
determinar si su último dígito es primo.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero % 4 == 0 and numero % 10 == 2 or numero % 10 == 3 or numero % 10 == 5 or numero % 10 == 7:
		print "El numero ingresado es multiplo de cuatro y ademas su ultimo digito es un numero primo."

	elif numero % 4 == 0 and numero % 10 != 2 or numero % 10 != 3 or numero % 10 != 5 or numero % 10 != 7:
		print "El numero ingresado es multiplo de cuatro pero su ultimo digito no es un numero primo."

	elif numero % 4 != 0 and numero % 10 == 2 or numero % 10 == 3 or numero % 10 == 5 or numero % 10 == 7:
		print "El numero ingresado no es multiplo de cuatro pero su ultimo digito si es un numero primo."

	else:
		print "El numero ingresado no es multiplo de cuatro y su ultimo digito no es un numero primo."

except ValueError:
	print "El numero digitado debe ser un valor numerico"