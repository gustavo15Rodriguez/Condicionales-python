#-*-coding:utf-8-*-

'''Leer dos números enteros de dos dígitos y determinar 
si la suma de los dos números
origina un número par.'''

try:
	numero1 = int(raw_input("Digite el primer numero: "))
	numero2 = int(raw_input("Digite el segundo numero: "))

	if numero1 > 9 and numero1 <= 99 and numero2 > 9 and numero2 <= 99:
		resultado = numero1 + numero2
		valor = resultado % 2 

		if valor == 0:
			print "El resultado de la suma origina un numero par."

		else:
			print "El resultado de la suma no origina un numero par."

	else:
		print "Ambos numeros deben ser de dos digitos."

except ValueError:
	print "El numero digitado debe ser un valor numerico"