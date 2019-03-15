#-*-coding:utf-8-*-

'''Leer un número entero de cuatro dígitos y 
determinar a cuanto es igual la suma de sus
dígitos.'''

try:
	numero = int(raw_input("Digite un numero de cuatro digitos: "))

	if numero > 999 and numero <= 9999:
		digito1 = numero / 1000
		digito2 = (numero % 1000) / 100
		digito3 = (numero % 100) / 10
		digito4 = numero % 10

		valor = digito1 + digito2 + digito3 + digito4
		print "El resultado de la suma de los cuatro digitos es %d"%valor

	else:
		print "El numero digitado debe poseer cuatro digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"	