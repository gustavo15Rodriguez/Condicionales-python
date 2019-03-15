#-*-coding:utf-8-*-

'''leer un número entero de dos dígitos 
y determinar a cuánto es igual la suma de 
sus dígitos.'''

try:
	numero = int(raw_input("Digite un numero de dos digitos: "))


	if numero  >= 10 and numero <= 99:
		entero = numero % 10
		digito_2 = numero / 10
		resultado = entero + digito_2
		print "El resultado es %d: "%resultado
	else:
		print "El numero ingresado debe poseer dos digitos"

except:
	ValueError = "El numero digitado debe ser un valor numerico"