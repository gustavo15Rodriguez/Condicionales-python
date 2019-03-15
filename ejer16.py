#-*-coding:utf-8-*-

'''Leer un número entero de tres dígitos y determinar 
si al menos dos de sus tres dígitos
son Iguales.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero > 99 and numero <= 999:
		digito_1 = numero / 100
		digito_2 = (numero % 100) / 10
		digito_3 = numero % 10
	
		if digito_1 == digito_2  and digito_2 == digito_3 and digito_3 == digito_1:
			print "Todos los digitos son iguales."

		elif digito_1 == digito_2 and digito_1 != digito_3:
			print "El digito %d"%digito_1 + " es igual al digito %d"%digito_2 + " pero el digito %d"%digito_1 + " es diferente al digito %d"%digito_3

		elif digito_1 != digito_2 and digito_1 == digito_3:
			print "El digito %d"%digito_1 + " es diferente al digito %d"%digito_2 + " pero el digito %d"%digito_1 + " es igual al digito %d"%digito_3

		elif digito_2 == digito_1 and digito_2 != digito_3:
			print "El digito %d"%digito_2 + " es igual al digito %d"%digito_1 + " pero el digito %d"%digito_2 + " es diferente al digito %d"%digito_3

		elif digito_2 != digito_1 and digito_2 == digito_3:
			print "El digito %d"%digito_2 + " es diferente al digito %d"%digito_1 + " pero el digito %d"%digito_2 + " es igual al digito %d"%digito_3

		else:
			print "Todos los digitos son diferentes"

	else:
		print "El numero ingresado debe poseer tres digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"