#-*-coding:utf-8-*-

'''Leer dos números enteros de dos dígitos y determinar si la diferencia entre los dos es un
número primo.'''

try:
	numero1 = int(raw_input("Digite el primer numero: "))
	numero2 = int(raw_input("Digite el segundo numero: "))

	if numero1 >= 10 and numero1 <= 99 and numero2 >= 10 and numero2 <= 99:
		resultado1 = numero1 - numero2
		resultado2 = numero2 - numero1

		if resultado1 %2 > 0:
			print "La diferencia entre los numeros es un numero primo"

		elif resultado2 %2 > 0:
			print "La diferencia entre los numeros es un numero primo"

		else:
			print "La diferencia entre los numeros no es un numero primo"

	else:
		print "Los numeros ingresados deben poseer dos digitos"


except ValueError:
	print "El numero digitado debe ser un valor numerico"