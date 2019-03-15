#-*-coding:utf-8-*-

'''Leer tres números enteros y 
determinar cuál es el mayor. Usar solamente dos variables'''

try:
	numero_1 = int(raw_input("Digite el primer numero: "))
	numero_2 = int(raw_input("Digite el segundo numero: "))

	numero_1 = numero_1 * 100
	numero_1 = numero_1 + numero_2

	numero_1 = numero_1 / 100
	
	numero_2 = numero_2 * 100
	numero_2 = numero_2 / 100
	
	if numero_1 > numero_2:

		numero_2 = int(raw_input("Digite otro numero: "))
		print "%d"%numero_2

		if numero_1 > numero_2:
			print "Es mayor el %d"%numero_1

		else:
			"Es mayor el %d"%numero_2

	elif numero_2 > numero_1:
		numero_1 = int(raw_input("Digite el numero: "))

		if numero_2 > numero_1:
			print "Es mayor el %d"%numero_2

		else:
			print "Es mayor el %d"%numero_1

	elif numero_1 == numero_2:
		numero_2 = int(raw_input("Digite un numero: "))

		if numero_1 > numero_2:
			print "El mayor es %d"%numero_1

		elif numero_1 == numero_2:
			print "Todos los numeros son iguales"

		else:
			print "El mayor es %d"%numero_2



except ValueError:
	print "El numero digitado debe ser un valor numerico"