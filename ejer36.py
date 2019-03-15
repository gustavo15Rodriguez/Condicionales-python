#-*-coding:utf-8-*-

'''Leer un número entero de 4 dígitos y determinar 
si tiene más dígitos pares o impares.'''

try:
	numero = int(raw_input("Digite un numero de cuatro digitos: "))

	if numero > 999 and numero <= 9999:
		d_1 = numero / 1000
		d_2 = (numero % 1000) / 100
		d_3 = (numero % 100) / 10
		d_4 = numero % 10

		if d_1%2 == 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 == 0:
			print "Todos los digitos son pares"

		elif d_1%2 == 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 != 0:
			print "La mayoria de los digitos son pares"

		elif d_1%2 == 0 and d_2%2 == 0 and d_3%2 != 0 and d_4%2 == 0:
			print "La mayoria de los digitos son pares"

		elif d_1%2 == 0 and d_2%2 != 0 and d_3%2 == 0 and d_4%2 == 0:
			print "La mayoria de los digitos son pares"

		elif d_1%2 != 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 == 0:
			print "La mayoria de los digitos son pares"

		elif d_1%2 != 0 and d_2%2 != 0 and d_3%2%2 == 0 and d_4%2 == 0:
			print "La mitad de digitos son pares"

		elif d_1%2 != 0 and d_2%2 == 0 and d_3%2 != 0 and d_4%2 == 0:
			print "La mitad de digitos son pares"

		elif d_1%2 == 0 and d_2%2 == 0 and d_3%2 != 0 and d_4%2 != 0:
			print "La mitad de digitos son pares"

		elif d_1%2 != 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 != 0:
			print "La mitad de digitos son pares"

		elif d_1%2 == 0 and d_2%2 != 0 and d_3%2 == 0 and d_4%2 != 0:
			print "La mitad de digitos son pares"

		elif d_1%2 == 0 and d_2%2 != 0 and d_3%2 != 0 and d_4%2 == 0:
			print "La mitad de digitos son pares"

		elif d_1%2 == 0 and d_2%2 != 0 and d_3%2 != 0 and d_4%2 != 0:
			print "La mayoria de digitos son impares"

		elif d_1%2 != 0 and d_2%2 == 0 and d_3%2 != 0 and d_4%2 != 0:
			print "La mayoria de digitos son impares"

		elif d_1%2 != 0 and d_2%2 != 0 and d_3%2 == 0 and d_4%2 != 0:
			print "La mayoria de digitos son impares"

		elif d_1%2 != 0 and d_2%2 != 0 and d_3%2 != 0 and d_4%2 == 0:
			print "La mayoria de digitos son impares"

		else:
			print "Todos los digitos son impares"

	else:
		print "El numero ingresado debe poseer cuatro digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"