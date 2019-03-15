#-*-coding:utf-8-*-

'''Leer un número entero de tres dígitos y 
determinar si algún dígito es múltiplo de los
otros.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero > 99 and numero <= 999:
		digito_1 = numero / 100
		digito_2 = (numero % 100) / 10
		digito_3 = numero % 10

		valor_1 = (digito_1 % digito_2) 
		Valor1 = (digito_1 % digito_2)
		valor_2 = (digito_2 % digito_1)
		Valor2 = (digito_2 % digito_3)
		valor_3 = (digito_3 % digito_2)
		Valor3 = (digito_3 % digito_1)

		if valor_1 == 0:
			print "El digito %d"%digito_1 + " es multiplo del digito %d"%digito_2 + " y el digito %d"%digito_1 + " es multiplo del digito %d"%digito_3

		elif Valor1 == 0:
			print "El digito %d"%digito_1 + " es multiplo del digito %d"%digito_3

		elif valor_2 == 0:
			print "El digito %d"%digito_2 + " es multiplo del digito %d"%digito_1

		elif Valor2 == 0:
			print "El digito %d"%digito_2 + " es multiplo del digito %d"%digito_3

		elif valor_3 == 0:
			print "El digito %d"%digito_3 + " es multiplo del digito %d"%digito_2

		elif Valor3 == 0:
			print "El digito %d"%digito_3 + " es multiplo del digito %d"%digito_1

		elif valor_1 == 0 and valor1 == 0 and valor_2 == 0 and Valor2 == 0 and valor_3 == 0 and Valor3 == 0:
			print "Todos los digitos son multiplos entre si"
		
		elif valor_1 != 0 and Valor1 != 0 and valor_2 != 0 and Valor2 != 0 and valor_3 != 0 and Valor3 != 0:
			print "Ninguno de los digitos son multiplos entre si"

	else:
		print "El numero debe ser mayor de 99 y menor de 1000"

except ValueError:
	print "El numero digitado debe ser un valor numerico"