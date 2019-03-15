#-*-coding:utf-8-*-

'''Leer un número entero y si es múltiplo de 4 mostrar en pantalla su mitad, si es múltiplo
de 5 mostrar en pantalla su cuadrado y si es múltiplo de 6 mostrar en pantalla su primer
dígito. Asumir que el número no es mayor que 100.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero > 0 and numero <= 100:
		v1 = numero / 100
		v2 = (numero / 100) % 10
		v3 = numero % 10

		r1 = numero / 2
		r2 = numero * numero 
		r3 = v2

		if  numero % 4 == 0:
			print "El numero es multiplo de cuatro y su mitad es %d"%r1

		elif numero % 5 == 0:
			print "El numero es multiplo de cinco y su cuadrado es %d"%r2

		elif numero % 6 == 0:
			print "El numero es multiplo de seis y el primer digito es %d"%v1

		else:
			print "El numero ingresado no es multiplo ni de cuatro, ni de cinco, ni de seis."

	else:
		print "El numero ingresado no debe ser mayor a cien."		

except ValueError:
	print "El numero digitado debe ser un valor numerico"