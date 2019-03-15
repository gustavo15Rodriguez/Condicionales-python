#-*-coding:utf-8-*-

'''Leer un número entero de dos dígitos 
menor que 20 y determinar si es primo.'''

try:
	numero = int(raw_input("Digite un numero entero menor a 20: "))

	if numero >= 1 and numero < 20:

		if ((numero == 2) or (numero == 3) or (numero == 5) or (numero == 7) or (numero == 11) or (numero == 13) or (numero == 17) or (numero == 19)):
			print "El numero digitado es primo."

		else:
			print "El numero digitado no es primo."

	else:
		print "Debe ingresar dos digitos menores que 20."

except:
	ValueError = "El numero digitado debe ser un valor numerico"