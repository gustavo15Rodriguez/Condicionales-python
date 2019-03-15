#-*-coding:utf-8-*-

'''Leer dos números enteros y 
determinar cuál es el mayor.'''

try:
	numero_1 = int(raw_input("Digite el primer numero: "))
	numero_2 = int(raw_input("Digite el segundo numero: "))

	if numero_1 > numero_2:
		print "El numero %d"%numero_1 + " es mayor al numero %d"%numero_2

	elif numero_2 > numero_1:
		print "El numero %d"%numero_2 + " es mayor al numero %d"%numero_1

	elif numero_1 == numero_2:
		print "Ambos numeros son iguales"

	else:
		print "Debe ingresar dos numeros positivos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"