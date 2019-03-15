#-*-coding:utf-8-*-

'''Leer un número entero de dos 
dígitos y determinar si sus dos dígitos son primos'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero > 9 and numero <= 99:
		digito1 = numero / 10
		digito2 = numero % 10

		if ((digito1 == 2) or (digito1 == 3) or (digito1 == 5) or (digito1 == 7)):
			print "El primer digito es primo"


		if ((digito2 == 2) or (digito2 == 3) or (digito2 == 5) or (digito2 == 7)):
			print "El segundo digito es primo"

		else:
			print "Ninguno de los dos digitos es primo."
	
	else:
		print "Debe ingresar un numero de dos digitos."

except ValueError:
	print "El numero digitado debe ser un valor numerico"