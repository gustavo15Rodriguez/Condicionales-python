#-*-coding:utf-8-*-

'''Leer un número entero de tres dígitos y 
determinar cuántos dígitos pares tiene.'''

try:
	numero = int(raw_input("Digite un numero de tres digitos: "))

	if numero > 99 and numero <= 999:
		digito1 = numero / 100
		digito2 = (numero % 100) / 10
		digito3 = numero % 10

		if digito1%2 == 0 and digito2%2 == 0 and digito3%2 == 0:
			print "Todos los digitos son pares"

		elif digito1%2 == 0 and digito2%2 != 0 and digito3%2 != 0:
			print "Solo hay un digito par y es el primero"

		elif digito1%2 != 0 and digito2%2 == 0 and digito3%2 != 0:
			print "Solo hay un digito par y es el segundo"

		elif digito1%2 != 0 and digito2%2 != 0 and digito3%2 == 0:
			print "Solo hay un digito par y es el tercero"

		elif digito1%2 == 0 and digito2%2 == 0 and digito3%2 != 0:
			print "Solo hay dos digitos pares que son el primero y el segundo"

		elif digito1%2 == 0 and digito2%2 != 0 and digito3%2 == 0:
			print "Solo hay dos digitos pares que son el primero y el tercero"

		elif digito1%2 != 0 and digito2%2 == 0 and digito3%2 == 0:
			print "Solo hay dos digitos pares que son el segundo y el tercero"

		else:
			print "No hay digitos pares"

	else:
		print "El numero digitado debe poseer tres digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"	