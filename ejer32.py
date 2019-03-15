#-*-coding:utf-8-*-

'''Leer un número entero y 
determinar si es múltiplo de 7.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero%7 == 0:
		print "El numero %d"%numero + " es multiplo de 7"

	else:
		print "El numero %d"%numero + " no es multiplo de 7"


except ValueError:
	print "El numero digitado debe ser un valor numerico"