#-*-coding:utf-8-*-

'''Leer un número entero de tres dígitos y 
determinar cuántos dígitos primos tiene.'''

try:
	numero = int(raw_input("Digite un numero de tres digitos: "))

	if numero > 99 and numero <= 999:

		digito1 = numero / 100
		digito2 = (numero % 100) / 10
		digito3 = numero % 10

		cont = 0 

		if (digito1 == 2 or digito1 == 3 or (digito1 %2 != 0 and digito1%3 != 0)) and digito1 != 1:
			cont += 1

		if (digito2 == 2 or digito2 == 3 or (digito2 %2 != 0 and digito2 %3 != 0)) and digito2 != 1:
			cont +=1

		if (digito3 == 2 or digito3 == 3 or (digito3 %2 != 0 and digito3 %3 != 0)) and digito3 != 1:
			cont +=1

		print "el numero %i tiene %i primos"%(numero,cont)

	else:
		print "El numero ingresado debe poseer tres digitos."

except ValueError:
	print "El numero digitado debe ser un valor numerico"	