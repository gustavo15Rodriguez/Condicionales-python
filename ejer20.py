#-*-coding:utf-8-*-

'''Leer tres números enteros y mostrarlos 
ascendentemente.'''

try:
	numero_1 = int(raw_input("Digite el primer numero: "))
	numero_2 = int(raw_input("Digite el segundo numero: "))
	numero_3 = int(raw_input("Digite el tercer numero: "))

	if numero_1 < numero_2 and numero_2 < numero_3:
		print (str (numero_1), str (numero_2), str (numero_3))

	elif numero_1 < numero_2 and numero_3 < numero_2:
		print (str (numero_1), str (numero_3), str (numero_2))

	elif numero_2 < numero_1 and numero_1 < numero_3:
		print (str (numero_2), str (numero_1), str (numero_3))

	elif numero_3 < numero_1 and numero_1 < numero_2:
		print (str (numero_3), str (numero_1), str (numero_2))

	elif numero_1 < numero_2 and numero_2 < numero_3:
		print (str (numero_1), str (numero_3), str (numero_2))

	elif numero_3 < numero_2 and numero_2 < numero_1:
		print (str (numero_3), str (numero_2), str (numero_1))


	else:
		print "El numero debe ser mayor de 1"

except ValueError:
	print "El numero digitado debe ser un valor numerico"