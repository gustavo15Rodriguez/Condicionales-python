#-*-coding:utf-8-*-

'''Leer un número entero y determinar 
si es negativo.'''

try:
	numero = int(raw_input("Digite el valor deseado: "))

	if numero < 0:
		print "El numero digitado es negativo."

	else:
		print "El numero digitado no es negativo."

except:
	ValueError = "El numero digitado debe ser un valor numerico"