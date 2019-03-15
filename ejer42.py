#-*-coding:utf-8-*-

'''Leer dos números enteros y determinar si 
la diferencia entre los dos es un número par.'''

try:
	numero1 = int(raw_input("Digite el primer numero: "))
	numero2 = int(raw_input("Digite el segundo numero: "))

	if numero1 > 0 and numero2 > 0:
		r1 = numero1 - numero2
		r2 = numero2 - numero1
		
		if r1 %2 == 0:
			print "La diferencia entre los numeros es un numero par"

		elif r2 %2 == 0:
			print "La diferencia entre los numeros es un numero par"

		else:
			print "La diferencia entre los numeros no es un numero par"

	else:
		print "Los numeros ingresados deben ser positivos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"