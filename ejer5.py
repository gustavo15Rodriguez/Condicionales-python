#-*-coding:utf-8-*-

'''Leer un número entero 
de dos dígitos y determinar si ambos 
dígitos son pares.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))

	if numero >= 10 and numero <= 99:
		digito_1 = numero / 10
		digito_2 = numero % 10 

	if digito_1 % 2 == 0 and digito_2 % 2 == 0:
		print "Ambos digitos son pares. "

	elif digito_1 % 2 == 0 and digito_2 % 2 != 0:
		print " El primer digito es par y el segundo digito es impar."

	elif digito_1 % 2 != 0 and digito_2 % 2 == 0:
		print "El primer digito es impar y el segundo digito es par."

	else:
		print "Ninguno de los digitos es par."

except:
	ValueError = "El numero digitado debe ser un valor numerico"