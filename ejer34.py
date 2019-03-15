#-*-coding:utf-8-*-

'''Leer un número entero menor que mil y 
determinar cuántos dígitos tiene.'''

try:
	numero = int(raw_input("Digite un numero menor a mil: "))

	if numero >= 100 and numero <= 999:
		print "El numero ingresado posee tres digitos"

	elif numero >= 10 and numero <= 99:
		print "El numero ingresado posee dos digitos"

	elif numero > 0 and numero <= 9:
		print "El numero ingresado posee un digito"

	else:
		print "El numero ingresado debe ser menor a mil"

except ValueError:
	print "El numero digitado debe ser un valor numerico"