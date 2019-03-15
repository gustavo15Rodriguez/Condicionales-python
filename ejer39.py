#-*-coding:utf-8-*-

'''Leer tres números enteros de tres dígitos y determinar si el 
penúltimo dígito de los tres números es igual.'''

try:
	numero1 = int(raw_input("Digite el primer numero: "))
	numero2 = int(raw_input("Digite el segundo numero: "))
	numero3 = int(raw_input("Digite el tercer numero: "))

	if numero1 > 99 and numero1 <=999 and numero2 > 99 and numero2 <=999 and numero3 > 99 and numero3 <=999:

		d1 = (numero1 % 100) / 10
		d2 = (numero2 % 100) / 10
		d3 = (numero3 % 100) / 10

		if d1 == d2 and d1 == d3:
			print "El penultimo digito de los tres numeros es igual"

		elif d1 == d2 and d2 != d3:
			print "Solo el penultimo digito del primer y segundo numero son iguales"

		elif d1 != d2 and d1 == d3:
			print "Solo el penultimo digito del primer y tercer numero son iguales"

		elif d2 != d1 and d2 == d3:
			print "Solo el penultimo digito del segundo y tercer numero son iguales"

		else:
			print "Ninguno de los penultimos digitos de los tres numeros coinciden"

	else:
		print "Los numeros deben ser de tres digitos."

except ValueError:
	print "El numero digitado debe ser un valor numerico"