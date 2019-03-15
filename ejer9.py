#-*-coding:utf-8-*-

'''Leer un número entero de dos dígitos y 
determinar si un dígito es múltiplo del otro'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero > 9 and numero <=99:
		digito1 = numero / 10
		digito2 = numero % 10
		valor_1 = digito1%digito2
		valor_2 = digito2%digito1

		if valor_1 == 0:
			print "El %d"%digito1 + " es multiplo del %d"%digito2

		elif valor_2 == 0:
			print "El %d"%digito2 + " es multiplo del %d"%digito1

		elif valor_1 != 0 and valor_2 != 0:
			print "Ninguno de los digitos son multiplos"

	else:
		print "El numero debe ser mayor de 9 y menor de 100"



except ValueError:
	print "El numero digitado debe ser un valor numerico"