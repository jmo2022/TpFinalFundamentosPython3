#Creo la lista del stock:

import ast

stock=open("stock_completo.txt", 'r')

stock_completo=stock.read()

stock.close()

if stock_completo != "":

	stock_completo=ast.literal_eval(stock_completo)
	
else:
	
	stock_completo=[]


#Creo los items:

def crear_item(lista):
	
	nombre=input("Ingrese el nombre del item o \"fin\" para salir: \n")
	nombre1=nombre.upper()
	while nombre1 != "FIN":
		item=[]
		item.append(nombre1)
		
		codigo=input("Ingrese el codigo del item (numerico): \n")
		codigo=int(codigo)
		item.append(codigo)
		
		talle=input("Ingrese talle del item(XS,S,M,L,XL,XXL): \n")
		talle1=talle.upper()
		print(type(talle1))
		item.append(talle1)
		
		cantidad=input("Ingrese la cantidad del item (numerico): \n")
		cantidad=int(cantidad)
		item.append(cantidad)
		
		lista.append(item)
		
		nombre=input("Ingrese el nombre del item o \"fin\" para salir: \n")
		nombre1=nombre.upper()
		
		
	
		
	return lista

	
#Modifico stock:

def modifico_stock(lista,item,stock):
	
	contador = False
	
	if type(item) == int:
		for i in lista:
			if i[1] == item:
				i[3] = stock
				contador=True

			
	elif type(item) == str:
		item1=item.upper()
		for i in lista:
			if i[0] == item1:
				i[3] = stock
				contador=True

	if contador == False:
		print ("-" * 20)
		print("\n")
		print("El item ingresado no se encuentra.")
		print("\n")
		print ("-" * 20)
		menu()
		
	else:

		return lista


#Borro item:


def borrar_item(lista,item):
	
	contador = False
	
	if type(item) == int:
		for i in lista:
			if i[1] == item:
				lista.remove(i)
				contador=True

	elif type(item) == str:
		item1=item.upper()
		for i in lista:
			if i[0] == item1:
				lista.remove(i)
				contador=True

	
	
	if contador == False:
		print ("-" * 20)
		print("\n")
		print("El item ingresado no se encuentra.")
		print("\n")
		print ("-" * 20)
		menu()
		
	else:

		return lista
	
#Cambio nombre de item:

def cambio_nombre(lista,item,nombre):
	
	contador = False
	
	if type(item) == int:
		nombre1=nombre.upper()
		for i in lista:
			if i[1] == item:
				i[0] = nombre1
				contador=True

	elif type(item) == str:
		nombre1=nombre.upper()
		item1=item.upper()
		for i in lista:
			if i[0] == item1:
				i[0] = nombre1
				contador=True
	
	if contador == False:
		print ("-" * 20)
		print("\n")
		print("El item ingresado no se encuentra.")
		print("\n")
		print ("-" * 20)
		menu()
		
	else:

		return lista
	
#Cambio codigo de item:

def cambio_codigo(lista,item,codigo):
	
	contador = False
	
	if type(item) == int:
		
		for i in lista:
			if i[1] == item:
				i[1] = codigo
				contador=True
				 
				


	elif type(item) == str:
		item1=item.upper()
		for i in lista:
			if i[0] == item1:
				i[1] = codigo
				contador=True
				
	

	if contador == False:
		print ("-" * 20)
		print("\n")
		print("El item ingresado no se encuentra.")
		print("\n")
		print ("-" * 20)
		menu()
		
	else:

		return lista

#Cambio talle de item:

def cambio_talle(lista,item,talle):
	talle1=talle.upper()
	contador = False
	
	if type(item) == int:		
		for i in lista:			
			if i[1] == item:
				i[2] = talle1
				contador=True

	elif type(item) == str:
		item1=item.upper()
		
		for i in lista:
			if i[0] == item1:
				i[2] = talle1
				contador=True
				
	if contador == False:
		print ("-" * 20)
		print("\n")
		print("El item ingresado no se encuentra.")
		print("\n")
		print ("-" * 20)
		menu()
		
	else:

		return lista

#Mostrar item:

def muestro_item(lista,item):
	
	contador = False
	if type(item) == int:
		for i in lista:
			if i[1] == item:
				print ("-" * 20)
				print("\n")
				print ("Item: " + i[0])
				print ("Codigo: " + str(i[1]))
				print ("Talle: " + (i[2]))
				print ("Cantidad :"+ str(i[3]))
				print("\n")
				print ("-" * 20)
				contador=True

	elif type(item) == str:
		item1=item.upper()
		for i in lista:
			if i[0] == item1:
				print ("-" * 20)
				print("\n")
				print ("Item: " + i[0])
				print ("Codigo: " + str(i[1]))
				print ("Talle: " + (i[2]))
				print ("Cantidad :"+ str(i[3]))
				print("\n")
				print ("-" * 20)
				contador=True
				
	if contador == False:
		print ("-" * 20)
		print("\n")
		print("El item ingresado no se encuentra.")
		print("\n")
		print ("-" * 20)
		menu()
				
#Mostrar todos los items:

def muestro_todo(lista):
	
	for i in lista:
		print("\n")
		print ("Item: " + i[0])
		print ("Codigo: " + str(i[1]))
		print ("Talle: " + (i[2]))
		print ("Cantidad :"+ str(i[3]))
		print("\n")
		print ("-" * 20)
	menu()	

#Pantalla bienvenida:

print("\n")
print (" " * 15 + "Bienvenido")
print(" \n " + "-" * 40 )

#Menu:

def menu():
	
	print("\n")
	print("Elija que accion desea realizar: ")
	print("\n")
	print("1 - Mostrar todos los items del stock.")
	print("2 - Mostrar un item en particular.")
	print("3 - Crear un item. ")
	print("4 - Modificar cantidad de un item.")
	print("5 - Modificar talle de un item.")
	print("6 - Modificar codigo de un item.")
	print("7 - Modificar nombre de un item.")
	print("8 - Borrar un item.")
	print("9 - Salir.")
	print("\n")
	print(" \n " + "-" * 40 )
	seleccion=input("Ingrese la opcion deseada:")
	seleccion=int(seleccion)
	print(" \n " + "-" * 20 )
	
	

	
	if seleccion <= 9 and seleccion > 0 :
		
		#Opcion 1:
		
		if seleccion == 1:
			print("\n")
			muestro_todo(stock_completo)
			print("\n")
		
		#Opcion 2:
		
		elif seleccion == 2:
			print("\n")
			print("-Para seleccionar item por nombre ingrese 1 ")
			print("-Para seleccionar item por codigo ingrese 2 ")
			select=input("")
			select=int(select)
			print("\n")
			if select < 3 and select > 0:
				if select == 1:
					print("\n")
					sel=input("Ingrese el nombre del item: ")
					muestro_item(stock_completo,sel)
					print("\n")
					
				else:
					print("\n")
					sel=input("Ingrese codigo del item: ")
					sel=int(sel)
					muestro_item(stock_completo,sel)
					print("\n")
					

		
			else:
				print("\n")
				print ("-" * 20)
				print(str(select) + " no es una opcion valida.")
				print ("-" * 20)
				print("\n")
				menu()
		
		#Opcion 3:		
				
		elif seleccion == 3:
			
			l=crear_item(stock_completo)
			
			
			
		
		#Opcion 4:
		
		elif seleccion == 4:
			
			print("\n")
			print ("-" * 20)						
			print("-Para identificar item con codigo ingrese 1")
			print("-Para identificar item con nombre ingrese 2")
			sel=input("-")
			sel=int(sel)
			print ("-" * 20)
				
			if sel == 1 or sel == 2:
				
				if sel == 1:
					
					s=input("Ingrese codigo del item: ")
					s=int(s)
					
					c=input("Ingrese la nueva cantidad: ")
					c=int(c)
					
					
					modifico_stock(stock_completo,s,c)
					
					
					
				elif sel == 2:
					
					s=input("Ingrese codigo del item: ")
					
					c=input("Ingrese la nueva cantidad: ")
					c=int(c)
					
					modifico_stock(stock_completo,s,c)	
			else:
				
				
				print("La opcion " + str(sel)+" no es correcta.")
				
				print ("-" * 20)
				
				menu()
			
		#Opcion 5:	
		
		elif seleccion == 5:
			
					
			print("\n")
			print ("-" * 20)						
			print("-Para identificar item con codigo ingrese 1")
			print("-Para identificar item con nombre ingrese 2")
			sel=input("-")
			sel=int(sel)
			print ("-" * 20)
				
			if sel == 1 or sel == 2:
				
				if sel == 1:
					
					s=input("Ingrese codigo del item: ")
					s=int(s)
					
					t=input("Ingrese el nuevo talle (s,m,l,xxl): ")
					t=t.upper()
					
					
					cambio_talle(stock_completo,s,t)	
					
				elif sel == 2:
					
					s=input("Ingrese nombre del item: ")
					s=s.upper()
					
					t=input("Ingrese el nuevo talle (s,m,l,xxl): ")
					t=t.upper()
					
					
					cambio_talle(stock_completo,s,t)
			else:
				
				
				print("La opcion " + str(sel)+" no es correcta.")
				
				print ("-" * 20)
				
				menu()
						
			
		#Opcion 6:
	
		elif seleccion == 6:
			
					
			print("\n")
			print ("-" * 20)						
			print("-Para identificar item con codigo ingrese 1")
			print("-Para identificar item con nombre ingrese 2")
			sel=input("-")
			sel=int(sel)
			print ("-" * 20)
				
			if sel == 1 or sel == 2:
				
				if sel == 1:
					
					s=input("Ingrese codigo del item: ")
					s=int(s)
					
					t=input("Ingrese el nuevo codigo numerico: ")
					t=int(t)
					
					cambio_codigo(stock_completo,s,t)	
					
				elif sel == 2:
					
					s=input("Ingrese nombre del item: ")
					s=s.upper()
					
					t=input("Ingrese el nuevo codigo numerico: ")
					t=int(t)
					
					
					cambio_codigo(stock_completo,s,t)
			else:
				
				
				print("La opcion " + str(sel)+" no es correcta.")
				
				print ("-" * 20)
				
				menu()	
	
		#Opcion 7:
	
		elif seleccion == 7:
			
					
			print("\n")
			print ("-" * 20)						
			print("-Para identificar item con codigo ingrese 1")
			print("-Para identificar item con nombre ingrese 2")
			sel=input("-")
			sel=int(sel)
			print ("-" * 20)
				
			if sel == 1 or sel == 2:
				
				if sel == 1:
					
					s=input("Ingrese codigo del item: ")
					s=int(s)
					
					t=input("Ingrese el nuevo nombre para el item: ")
					t=t.upper()
					
					cambio_nombre(stock_completo,s,t)
					
				elif sel == 2:
					
					s=input("Ingrese nombre del item: ")
					s=s.upper()
					
					t=input("Ingrese el nuevo nombre para el item: ")
					t=t.upper()
					
					
					cambio_nombre(stock_completo,s,t)
			else:
				
				
				print("La opcion " + str(sel)+" no es correcta.")
				
				print ("-" * 20)
				
				menu()	
	
	
		#Opcion 8:
	
		
		elif seleccion == 8:
			
					
			print("\n")
			print ("-" * 20)						
			print("-Para identificar item con codigo ingrese 1")
			print("-Para identificar item con nombre ingrese 2")
			sel=input("-")
			sel=int(sel)
			print ("-" * 20)
				
			if sel == 1 or sel == 2:
				
				if sel == 1:
					
					s=input("Ingrese codigo del item a borrar: ")
					s=int(s)
					
					borrar_item(stock_completo,s)
					
				elif sel == 2:
					
					s=input("Ingrese nombre del item a borrar: ")
					s=s.upper()
					
			
					borrar_item(stock_completo,s)
					

				
			else:
				
				
				print("La opcion " + str(sel)+" no es correcta.")
				
				print ("-" * 20)

		
				menu()	
	
	
	
		elif seleccion == 9:
				
			print("Hasta luego!")	
			
			
			exit()	
			
			
		#Se carga la lista al txt:	

		stockeado=str(stock_completo)
		stock=open("stock_completo.txt", 'w')
		stock.write(stockeado)
		stock.close()
		
		menu()
			
	#Opcion menu invalida:
	
	
	else:
		print("\n")
		print ("-" * 20)
		print(str(seleccion)+" no es una opcion valida.")
		print ("-" * 20)
		
		menu()
	

	
	
print(menu())










