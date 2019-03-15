#-*-coding:utf-8-*-

'''Leer un número entero de dos dígitos y determinar si es 
primo y además si es negativo.'''

try:
	numero = int(raw_input("Digite un numero de dos digitos: "))

	if numero > 0:

		if ((numero == 11) or (numero == 13) or (numero == 17) or (numero == 19) or (numero == 23) or (numero == 29) or (numero == 31) or (numero == 37) or (numero == 41) or (numero == 43) or (numero == 47) or (numero == 53) or (numero == 59) or (numero == 61) or (numero == 71) or (numero == 73) or (numero == 79) or (numero == 83) or (numero == 89) or (numero == 97)):
			print "El numero digitado es primo y es positivo"

		else:
			print "El numero digitado no es primo."

	if numero < 0:

		if ((numero == -11) or (numero == -13) or (numero == -17) or (numero == -19) or (numero == -23) or (numero == -29) or (numero == -31) or (numero == -37) or (numero == -41) or (numero == -43) or (numero == -47) or (numero == -53) or (numero == -59) or (numero == -61) or (numero == -71) or (numero == -73) or (numero == -79) or (numero == -83) or (numero == -89) or (numero == -97)):
			print "El numero digitado es primo y es negativo."

		else:
			print "El numero digitado no es primo."
		
	else:
		print "El numero ingresado debe ser de dos digitos."

	
except ValueError:
	print "El numero digitado debe ser un valor numerico"