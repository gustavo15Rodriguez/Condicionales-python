#-*-coding:utf-8-*-

'''Leer dos números enteros y determinar si la diferencia entre los dos es un número divisor
exacto de alguno de los dos números.'''

try:
	numero1 = int(raw_input("Digite el primer numero: "))
	numero2 = int(raw_input("Digite el segundo numero: "))

	if numero1 > 0 and numero2 > 0:
		r1 = numero1 - numero2
		r2 = numero2 - numero1

		if numero1 % r1 == 0:
			print "La diferencia que hay entre los numeros es un divisor exacto del primer numero"

		elif numero2 % r2 == 0:
			print "La diferencia que hay entre los numeros es un divisor exacto del segundo numero"

		else:
			print "La diferencia entre ambos numeros no origina un divisor de nunguno de los numeros"

	else:
		print "El numero ingresado debe ser positivo"

except ValueError:
	print "El numero digitado debe ser un valor numerico"