#-*-coding:utf-8-*-

'''Leer tres números enteros de dos dígitos cada uno y 
determinar en cuál de ellos se
encuentra el mayor dígito.'''

try:
	numero_1 = int(raw_input("Digite el primer numero: "))
	numero_2 = int(raw_input("Digite el segundo numero: "))
	numero_3 = int(raw_input("Digite el tercer numero: "))

	if numero_1 > 9 and numero_1 <= 99 and numero_2 > 9 and numero_2 <= 99 and numero_3 > 9 and numero_3 <=99:

		digito_a = numero_1 / 10
		digito_b = numero_1 % 10

		digito_c = numero_2 / 10
		digito_d = numero_2 % 10


		digito_e = numero_3 / 10
		digito_f = numero_3 % 10


		if digito_a > digito_b and digito_a > digito_c and digito_a > digito_d and digito_a > digito_e and digito_a > digito_f:
			print  "El digito mayor es %d"%digito_a + " y se encuentra en el primer numero ingresado"

		elif digito_b > digito_a and digito_b > digito_c and digito_b > digito_d and digito_b > digito_e and digito_b > digito_f:
			print "El digito mayor es %d"%digito_b + " y se encuentra en el primer numero ingrtesado"

		elif digito_c > digito_a and digito_c > digito_b and digito_c > digito_d and digito_c > digito_e and digito_c > digito_f:
			print "El digito mayor es %d"%digito_c + " y se encuentra en el segundo numero ingresado"

		elif digito_d > digito_a and digito_d > digito_b and digito_d > digito_c and digito_d > digito_e and digito_d > digito_f:
			print "El digito mayor es %d"%digito_d + " y se encuentra en el segundo numero ingresado"

		elif digito_e > digito_a and digito_e > digito_b and digito_e > digito_c and digito_e > digito_d and digito_e > digito_f:
			print "El digito mayor es %d"%digito_e + " y se encuentra en el tercer numero ingresado"

		elif digito_f > digito_a and digito_f > digito_b and digito_f > digito_c and digito_f > digito_d and digito_f > digito_e:
			print "El digito mayor es %d"%digito_f + " y se encuentra en el tercer numero ingresado"

		elif digito_c > digito_a and digito_c > digito_b and digito_c == digito_d and digito_e == digito_f:
			print "El segundo numero y el tercer numero son iguales"

		elif digito_a == digito_b and digito_c == digito_d and digito_c > digito_e and digito_c > digito_f:
			print "El primer numero y el segundo numero son iguales"

		elif digito_a == digito_b and digito_a > digito_c and digito_b > digito_c and digito_a > digito_d and  digito_b > digito_d and digito_a > digito_e and digito_b > digito_e and digito_a > digito_f and digito_b > digito_f:
			print "El primer numero es igual y mayor a los otros dos numeros"

		elif digito_c == digito_d and digito_c > digito_a and digito_d > digito_a and digito_c > digito_b and  digito_d > digito_b and digito_c > digito_e and digito_d > digito_e and digito_c > digito_f and digito_d > digito_f:
			print "El segundo numero es igual y mayor a los otros dos numeros"

		elif digito_a == digito_b and digito_a > digito_c and  digito_a > digito_d and digito_a > digito_c and  digito_b > digito_d and digito_e == digito_f:
			print "El primer numero y el tercer numero son iguales"

		elif digito_e == digito_f and digito_e > digito_a and digito_f > digito_a and digito_e > digito_b and  digito_f > digito_b and digito_e > digito_c and digito_f > digito_c and digito_e > digito_d and digito_f > digito_d:
			print "El tercer numero es igual y mayor a los otros dos numeros"

		else:
			print "Todos los digitos son iguales"

	else:
		print "Los numeros ingresado debe poseer dos digitos"

except ValueError:
	print "El numero digitado debe ser un valor numerico"	