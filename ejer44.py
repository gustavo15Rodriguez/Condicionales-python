#-*-coding:utf-8-*-

'''Leer un número entero de 4 dígitos y determinar si el primer dígito es múltiplo de alguno
de los otros dígitos.'''

try:
	numero = int(raw_input("Digite un numero de cuatro digitos: "))

	if numero >= 1000 and numero < 9999:
		d_1 = numero / 1000
		d_2 = (numero % 1000) / 100
		d_3 = (numero % 100) / 10
		d_4 = numero % 10

		if d_1 % d_2== 0 and d_1 % d_3 == 0 and d_1 % d_4 == 0:
			print "El primer digito es multiplo de los otros tres digitos a la vez."

		elif d_1 % d_2 == 0:
			print "El primer digito es multiplo del segundo digito."

		elif d_1 % d_3 == 0:
			print "El primer digito es multiplo del tercer digito."

		elif d_1 % d_4 == 0:
			print "El primer digito es multiplo del cuarto digito."

		else:
			print "El primer digito no es multiplo de ninguno de los demas digitos."

	else:
		print "El numero ingresado debe poseer cuatro digitos."

except ValueError:
	print "El numero digitado debe ser un valor numerico"