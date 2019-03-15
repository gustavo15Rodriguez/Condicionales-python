#-*-coding:utf-8-*-

'''Leer un número entero de cuatro dígitos y 
determinar cuántos dígitos pares tiene.'''

try:
	numero = int(raw_input("Digite un numero de cuatro digitos: "))

	if numero > 999 and numero <= 9999:
		d_1 = numero / 1000
		d_2 = (numero % 1000) / 100
		d_3 = (numero % 100) / 10
		d_4 = numero % 10

		if d_1%2 == 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 == 0:
			print "El numero ingresado posee los cuatro digitos pares"

		elif d_1%2 == 0 and d_2%2 != 0 and d_3%2 != 0 and d_4%2 != 0:
			print "El numero ingresado solo posee un digito par y es el primer digito"

		elif d_1%2 != 0 and d_2%2 == 0 and d_3%2 != 0 and d_4%2 != 0:
			print "El numero ingresado solo posee un digito par y es el segundo digito"

		elif d_1%2 != 0 and d_2%2 != 0 and d_3%2 == 0 and d_4%2 != 0:
			print "El numero ingresado solo posee un digito par y es el tercer digito"

		elif d_1%2 != 0 and d_2%2 != 0 and d_3%2 != 0 and d_4%2 == 0:
			print "El numero ingresado solo posee un digito par y es el cuarto digito"

		elif d_1%2 == 0 and d_2%2 == 0 and d_3%2 != 0 and d_4%2 != 0:
			print "El numero ingresado posee dos digitos pares que son el primero y el segundo"

		elif d_1%2 == 0 and d_2%2 != 0 and d_3%2 == 0 and d_4%2 != 0:
			print "El numero ingresado posee dos digitos pares que son el primero y el tercero"

		elif d_1%2 == 0 and d_2%2 != 0 and d_3%2 != 0 and d_4%2 == 0:
			print "El numero ingresado posee dos digitos pares que son el primero y el cuarto"

		elif d_1%2 != 0 and d_2%2 == 0 and d_3%2 != 0 and d_4%2 == 0:
			print "El numero ingresado posee dos digitos pares que son el segundo y el cuarto"

		elif d_1%2 != 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 != 0:
			print "El numero ingresado posee dos digitos pares que son el segundo y el tercero"

		elif d_1%2 != 0 and d_2%2 != 0 and d_3%2 == 0 and d_4%2 == 0:
			print "El numero ingresado posee dos digitos pares que son el tercero y el cuarto"

		elif d_1%2 == 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 != 0:
			print "El numero ingresado posee tres digitos pares que son el primero, el segundo y el tercero"

		elif d_1%2 == 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 != 0:
			print "El numero ingresado posee tres digitos pares que son el primero, el segundo y el tercero"

		elif d_1%2 == 0 and d_2%2 == 0 and d_3%2 != 0 and d_4%2 == 0:
			print "El numero ingresado posee tres digitos pares que son el primero, el segundo y el cuarto"

		elif d_1%2 == 0 and d_2%2 != 0 and d_3%2 == 0 and d_4%2 == 0:
			print "El numero ingresado posee tres digitos pares que son el primero, el tercero y el cuarto"

		elif d_1%2 != 0 and d_2%2 == 0 and d_3%2 == 0 and d_4%2 == 0:
			print "El numero ingresado posee tres digitos pares que son el segundo, el tercero y el cuarto"

		else:
			print "Nungun digito es par"

	else:
		print "El numero digitado debe poseer cuatro digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"	