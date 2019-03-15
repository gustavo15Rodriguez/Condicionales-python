#-*-coding:utf-8-*-

'''Leer dos números enteros y si la diferencia entre los dos es menor o igual a 10 entonces
mostrar en pantalla todos los enteros comprendidos entre el menor y el mayor de los
números leídos.'''

try:
	n1 = int(raw_input("Digite el primer numero: "))
	n2 = int(raw_input("Digite el segundo numero: "))

	d1 = n1 - n2 
	
	if d1 <= 10:
		cont = n2

		if d1 == 0 or d1 == 1:
			print "No existe diferencia entre los numeros"

		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont

		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont

		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont

		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont


		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont

		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont

		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont

		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont

		if cont < n1 and cont != n1 - 1:
			cont += 1
			print "%d"%cont

	else:
		print "La diferencia entre ambos numeros no es de 10"



	if d1 >= -10:
		cont = n1

		if d1 == 0 or d1 == -1:
			print "No existe diferencia entre los numeros"

		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont

		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont

		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont

		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont


		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont

		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont

		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont

		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont

		if cont < n2 and cont != n2 - 1:
			cont += 1
			print "%d"%cont

	else:
		print "La diferencia entre ambos numeros no es de 10"


except ValueError:
	print "EL vavlor ingresado debe ser un valor numerico"