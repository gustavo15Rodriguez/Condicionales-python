#-*-coding:utf-8-*-

'''Leer un número entero de cuatro dígitos y 
determinar si el segundo dígito es igual al
penúltimo.'''

try:
	numero = int(raw_input("Digite un numero de cuatro digitos: "))

	if numero > 999 and numero <= 9999:
		d_1 = numero / 1000
		d_2 = (numero % 1000) / 100
		d_3 = (numero % 100) / 10
		d_4 = numero % 10

		if d_2 == d_3:
			print "El segundo digito es igual al penultimo digito"

		else:
			print "El segundo digito no es igual al penultimo digito"

	if numero < 0:
		d_1 = numero / 1000
		d_2 = (numero % 1000) / 100
		d_3 = (numero % 100) / 10
		d_4 = numero % 10

		if d_2 == d_3:
			print "El segundo digito es igual al penultimo digito"

		else:
			print "El segundo digito no es igual al penultimo digito"

	else:
		print "El numero digitado debe poseer cuatro digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"	