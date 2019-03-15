#-*-coding:utf-8-*-

'''Leer dos números enteros de dos dígitos cada uno y si la diferencia entre los dos
números es par mostrar en pantalla la suma de los dígitos de los números, si dicha diferencia
es un número primo menor que 10 entonces mostrar en pantalla el producto de los dos
números y si la diferencia entre ellos terminar en 4 mostrar en pantalla todos los dígitos por
separado el producto de sus dos dígitos.'''

try:
	n1 = int(raw_input("Digite el primer numero de dos digitos: "))
	n2 = int (raw_input("Digite el segundo numero de dos digitos: "))

	if n1 > 0 and n1 <= 99 and n2 > 0 and n2 <= 99:
		v1 = n1 / 10
		v2 = n1 %10

		r1 = n2 / 10
		r2 = n2 % 10

		s = v1 + v2 + r1 + r2

		s1 = v1 + v2
		s2 = r1 + r2

		p = n1 * n2

		d1 = n1 - n2
		d2 = n2 - n1

		if n1 - n2 == 0:
			print "la diferencia entre ambos numeros es un numero par, y el resultado de lo suma de sus digitos es %d"%s

		elif n2 - n1 == 0:
			print "la diferencia entre ambos numeros es un numero par, y el resultado de lo suma de sus digitos es %d"%s

		else:
			print "La diferencia entre los numeros no es un numero par"

		if v1 %2 < 10:
			print "La diferencia entre ambos numeros es un numero primo, y el producto de ambos numeros es igual a %d"%p

		elif v2 %2 < 10:
			print "La diferencia entre ambos numeros es un numero primo, y el producto de ambos numeros es igual a %d"%p

		else:
			print "El numero ingresado debe ser menor a 10"

		if v2 == 4:
			print "La diferencia entre ambos numeros es 4, y el producto de los dos digitos de cada numero es igual a %d"%s1 + " para el primer numero, y %d"%s2 + " para el segundo numero"

		elif r1 == 4:
			print "La diferencia entre ambos numeros es 4, y el producto de los dos digitos de cada numero es igual a %d"%s1 + " para el primer numero, y %d"%s2 + " para el segundo numero"

		else:
			print "El numero ingresado no termina en 4, la diferencia entre ambos numeros no es un numero par ni un numero primo menor a 10."

	else:
		print "El numero ingresado debe ser mayor a 0 y menor de 100."


except ValueError:
	print "El numero digitado debe ser un valor numerico"