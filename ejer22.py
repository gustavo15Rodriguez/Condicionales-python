#-*-coding:utf-8-*-

'''Leer un número entero de tres dígitos y 
determinar si el primer dígito es igual al último.'''

try:
	numero = int(raw_input("Digite un numero de tres digitos: "))

	if numero >99 and numero <=999:	
		digito1 = numero / 100
		digito2 = (numero % 100) / 10
		digito3 = numero % 10

		if digito1 == digito3 :
			print "El primer digito es igual al tercer digito"

		else:
			print "EL primer digito no es igual al tercer digito"
		
	else:
		print "El numero ingresado debe poseer tres digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"	