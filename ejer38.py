#-*-coding:utf-8-*-

'''Leer tres números enteros y determinar si el 
último dígito de los tres números es igual.'''

try:
	numero1 = int(raw_input("Digite el primer numero: "))
	numero2 = int(raw_input("Digite el segundo numero: "))
	numero3 = int(raw_input("Digite el tercer numero: "))

	d1 = numero1 % 10
	d2 = numero2 % 10
	d3 = numero3 % 10

	if d1 == d2 and d1 == d3:
		print "El ultimo digito de los tres numeros es igual"

	elif d1 == d2 and d2 != d3:
		print "Solo el ultimo digito del primer y segundo numero son iguales"

	elif d1 != d2 and d1 == d3:
		print "Solo el ultimo digito del primer y tercer numero son iguales"

	elif d2 != d1 and d2 == d3:
		print "Solo el ultimo digito del segundo y tercer numero son iguales"

	else:
		print "Ninguno de los digitos finales de los tres numeros coinciden"

except ValueError:
	print "El numero digitado debe ser un valor numerico"