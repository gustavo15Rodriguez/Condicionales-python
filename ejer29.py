#-*-coding:utf-8-*-

'''Leer un número entero de cinco dígitos y 
determinar si es un número capicúo. Ej. 15651,
59895.'''

try:
	numero = int(raw_input("Digite un numero de cinco digitos: "))

	if numero > 9999 and numero <= 99999:
		d1 = numero / 10000
		d2 = (numero % 10000) / 1000
		d3 = (numero % 1000) / 100
		d4 = (numero % 100) / 10
		d5 = numero % 10

		if d1 == d5 and d2 == d4:
			print "El numero ingresado es un numero capicuo"

		else:
			print "El numero ingresado no es un numero capicuo"

	else:
		print "El numero digitado debe poseer cinco digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"	