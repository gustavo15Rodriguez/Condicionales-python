#-*-coding:utf-8-*-

'''Leer dos números enteros 
de dos dígitos y determinar si tienen dígitos comunes.'''

try:
	numero_1 = int(raw_input("Digite el  primer numero: "))
	numero_2 = int(raw_input("Digite el segundo numero: "))

	digito_1 = numero_1 / 10
	digito_2 = numero_1 % 10

	digito1 = numero_2 / 10
	digito2 = numero_2 % 10

	if digito_1 == digito1 and digito_2 == digito2 and numero_1 > 9 and numero_1 <= 99 and numero_2 > 9 and numero_2 <= 99:
		print "Todos los digitos son comunes"

	elif digito_1 == digito1 and digito_2 != digito2:
		print "El digito %d"%digito_1 + " es igual al digito %d"%digito1 + " y el digito %d"%digito_2 + " es diferente al digito %d"%digito2

	elif digito_1 != digito1 and digito_2 == digito2:
		print "EL digito %d"%digito_1 + " es diferente al digito %d"%digito1 + " y el digito %d"%digito_2 +" es igual al digito %d"%digito2

	elif digito_1 == digito2 and digito_2 == digito1:
		print "El digito %d"%digito_1 + " es igual al digito %d"%digito2 + " y el digito %d"%digito_2 + " es igual al digito %d"%digito1
		
	elif digito_1 == digito2 and digito_2 != digito1:
		print "El digito %d"%digito_1 + " es igual al digito %d"%digito2 + " y el digito %d"%digito_2 + " es diferente al digito %d"%digito1

	elif digito_1 != digito2 and digito_2 == digito1:
		print "El digito %d"%digito_1 + " es diferente al digito %d"%digito2 + " y el digito %d"%digito_2 + " es igual al digito %d"%digito1

	elif digito_1 != digito1 and digito_2 != digito2:
		print "Ninguno de los digitos son comunes"
 
	else:
		print "Debe ingresar un numero menor de 99 y mayor de 9"


except ValueError:
	print "El numero digitado debe ser un valor numerico"