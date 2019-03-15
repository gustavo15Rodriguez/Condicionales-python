#-*-coding:utf-8-*-

'''Leer un número entero de 2 dígitos y si es par mostrar en pantalla la suma de sus dígitos,
si es primo y menor que 10 mostrar en pantalla su último dígito y si es múltiplo de 5 y menor
que 30 mostrar en pantalla el primer dígito.'''

try:
	numero = int(raw_input("Digite un numero de dos digitos: "))

	if numero > 0 and numero <= 99:
		d1 = numero / 10
		d2 = numero % 10

		v1 = d1 + d2

		if ((numero == 2) or (numero == 3) or (numero == 5) or (numero == 7)) and numero < 10:
	 		print "El numero %d"%numero + " es un numero primo"

		elif numero%2 != 2 or numero%2 != 3 or numero%2 != 5 or numero%2 != 7:
	 		print "El numero ingresado no es un numero primo"

		else:
	 		print "El numero ingresado debe ser menor de 10"

	 	if numero% 2 == 0 and numero > 0 and numero < 99:
	 		print "El numero %d"%numero + " es un numero par y la suma de sus digitos es igual a %d"%v1

	 	elif numero% 2 != 0:
	 		print "El numero ingresado no es un numero par"

	 	else:
	 		print "El numero ingresado debe ser de dos digitos"

	 	if numero % 5 == 0 and numero > 0 and numero < 30:
	 		print "El numero %d"%numero + " es multiplo de 5 y su primer digito es %d"%d1

	 	elif numero % 5 != 0:
	 		print "El numero ingresado no es multiplo de 5"

	 	else:
	 		print "El numero ingresado debe ser menor de 30"

	else:
	 	print "El numero ingresado debe poseer dos digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"