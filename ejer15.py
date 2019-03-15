#-*-coding:utf-8-*-

'''Leer un número entero de tres dígitos y 
determinar a cuánto es igual la suma de sus
dígitos.'''

try:
	numero = int(raw_input("Digite un numero de tres digitos: "))
	
	if numero > 99 and numero <= 999:

		d1 = numero / 100
		d2 = (numero / 10) % 10
		d3 = numero % 10

		Valor = d1 + d2 + d3
		print "EL resultado de la suma es igual a %d"%Valor

	else:
		print "Debe ingresar un numero de tres digitos."


except ValueError:
	print "El numero digitado debe ser un valor numerico"