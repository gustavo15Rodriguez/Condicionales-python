#-*-coding:utf-8-*-

'''Leer un número entero y si es menor 
que 100 determinar si es primo.'''

try:
	numero = int(raw_input("Digite el numero deseado: "))
	if numero > 0 and numero < 100:
		
		if numero == 2 or numero == 3 or numero == 5 or numero == 7 or numero == 13 or numero == 17 or numero == 19 or numero == 23 or numero == 29 or numero == 31 or numero == 37 or numero == 41 or numero== 43 or numero == 47 or numero == 53 or numero == 59 or numero == 61 or numero == 67 or numero == 71 or numero == 73 or numero == 79 or numero == 83 or numero == 89 or numero == 97:
			print "El numero es menor que 100 y ademas es  un numero primo"
 
		else:
			print "El numero ingresado no es un numero primo"

	else:
		print "El numero ingresado no cumple con la condicion anterior. (Ser menor que 100 para determinar si es un numero primo.)"

except ValueError:
	print "El numero digitado debe ser un valor numerico"