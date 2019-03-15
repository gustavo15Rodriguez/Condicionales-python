#-*-coding:utf-8-*-

'''Leer un número entero de dos 
dígitos y determinar si los dos dígitos son iguales.'''

try:
	numero = int(raw_input("Digite un numero de dos digitos: "))

	if numero > 9 and numero <= 99:
		digito_1 = numero / 10
		digito_2 = numero % 10

		if digito_1 == digito_2:
			print "Ambos digitos son iguales"

		elif digito_1 != digito_2:
			print "Los digitos no son iguales"

	else:
		print "Debe ingresar un numero de dos digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"