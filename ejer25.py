#-*-coding:utf-8-*-

'''Leer un número entero de tres dígitos y determinar si 
alguno de sus dígitos es igual a la
suma de los otros dos.'''

try:
	numero = int(raw_input("Digite un numero de tres digitos: "))

	if numero > 99 and numero <= 999:
		digito1 = numero / 100
		digito2 = (numero % 100) / 10
		digito3 = numero % 10

		if digito2 + digito3 == digito1:
			print "Al sumar el segundo y tercer digito la suma origina como resultado el primer digito"

		elif digito1 + digito3 == digito2:
			print "Al sumar el primer y tercer digito la suma origina como resultado el segundo digito"

		elif digito1 + digito2 == digito3:
			print "Al sumar el primer y segundo digito la suma origina como resultado el tercer digito"

		else:
			print "Ninguna suma origina como resultado uno de sus digitos"

	else:
		print "El numero digitado debe poseer tres digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"	