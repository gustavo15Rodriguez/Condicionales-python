#-*-coding:utf-8-*-

'''Leer dos números enteros y determinar cuál es 
múltiplo de cuál.'''

try:
	numero_1 = int(raw_input("Digite el primer numero: "))
	numero_2 = int(raw_input("Digite el segundo numero: "))

	if numero_1 % numero_2 == 0:
		print "El primer numero %d"%numero_1 + " es multiplo del segundo numero que es %d"%numero_2

	elif numero_2 % numero_1 == 0:
		print "El segundo numero %d"%numero_2 + " es multiplo del primer numero  que es %d"%numero_1

	else:
		print "Ninguno de los dos numeros son multiplos entre si"

except ValueError:
	print "El numero digitado debe ser un valor numerico"