#-*-coding:utf-8-*-

'''Leer dos números enteros de dos dígitos y 
determinar a cuánto es igual la suma de todos
los dígitos'''

try:
	numero_1 = int(raw_input("Digite el primer numero de dos digitos: "))
	numero_2 = int(raw_input("Digite el segundo numero de dos digitos: "))

	if numero_1 > 9 and numero_1 <= 99 and numero_2 > 9 and numero_2 <= 99:
		digito_1 = numero_1 / 10
		digito_2 = numero_1 % 10

		digito1 = numero_2 / 10
		digito2 = numero_2 % 10

		valor = digito_1 + digito_2 + digito1 + digito2
		print "El resultado de la suma de los cuatro digitos es %d"%valor

	else:
		print "Ambos numeros deben poseer dos digitos."

except ValueError:
	print "El numero digitado debe ser un valor numerico"