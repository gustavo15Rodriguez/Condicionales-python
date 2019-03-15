#-*-coding:utf-8-*-

'''Leer un número entero de dos dígitos, guardar cada dígito 
en una variable diferente y
luego mostrarlas en pantalla.'''

try:
	numero = int(raw_input("Digite numero de dos digitos: "))

	if numero > 9 and numero < 100:
		d_1 = numero / 10
		d_2 = numero % 10

		print "%d"%d_1
		print "%d"%d_2
	
	else:
		print "EL numero ingresado debe poseer dos digitos"

	
except ValueError:
	print "El numero digitado debe ser un valor numerico"