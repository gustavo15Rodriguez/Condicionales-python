#-*-coding:utf-8-*-

'''Leer un número entero de 2 dígitos y si termina en 1 mostrar en pantalla su primer dígito,
si termina en 2 mostrar en pantalla la suma de sus dígitos y si termina en 3 mostrar en
pantalla el producto de sus dos dígitos.'''

try:
	numero = int(raw_input("Digite un numero de dos digitos: "))

	d1 = numero / 10
	d2 = numero % 10

	if numero > 9 and numero <= 99:
		s1 = d1 + d2
		s2 = d1 * d2

		if d2 == 1:
			print "El primer digito de la operacion es %d"%d1

		elif d2 == 2:
			print "La suma de sus digitos es %d"%s1

		elif d2 == 3:
			print "La multiplicacion de los dos digitos es %d"%s2

		else:
			print "El numero digitado no termina en 2, ni en 3."

	else:
		print "El numero ingresado debe poseer dos digitos."

except ValueError:
	print "El numero digitado debe ser un valor numerico"