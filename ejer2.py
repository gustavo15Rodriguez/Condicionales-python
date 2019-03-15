#-*-coding:utf-8-*-

'''Leer un número entero y determinar si
tiene 3 dígitos.'''

try:
	numero = int(raw_input("Digite un numero de tres digitos: "))

	if numero >= 100 and numero < 1000:
		print "El numero digitado posee tres digitos"

	else:
		print "El numero digitado no posee tres digitos"

except:
	ValueError = "El numero digitado debe ser un valor numerico"