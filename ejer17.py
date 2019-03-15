#-*-coding:utf-8-*-

'''Leer un número entero de tres dígitos y 
determinar en qué posición está el mayor dígito.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero > 99 and numero <= 999:
		digito1 = numero / 100
		digito2 = (numero % 100) / 10
		digito3 = numero % 10

		if digito1 > digito2 and digito1 > digito3:
			print "El digito mayor es %d"%digito1 + " y esta ubicado en la primer posicion."

		elif digito2 > digito1 and digito2 > digito3:
			print "El digito mayor es %d"%digito2 + " y esta ubicado en la segunda posicion."

		elif digito3 > digito1 and digito3 > digito2:
			print "El digito mayor es %d"%digito3 + " y esta ubicado en la tercer posicion."

		else:
			print "Todos los digitos son iguales"

	else:
		print "El numero ingresado debe poseer tres digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"