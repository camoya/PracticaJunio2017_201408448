import ListaUsuario
import Archivo
import Pila
A = Archivo
LU = ListaUsuario
P = Pila
class IU:
	def __init__(self):
		self.__logeado=False
		self.__nick = ""
		self.__log = None
		self.__LU = LU.ListaUsuario()
	def menuGeneral(self):
		opc = 0
		while (opc != 3):
			print("\n-------------- Menu Principal --------------")
			print("Cristhofer Alexander Moya Contreras - 201408448")
			print("Practica 1 [EDD] Junio 2017\n")
			print("1.- Usuarios")
			print("2.- Ingresar al sistema")
			print("3.- Salir del sistema\n")
			opc = int(input("Ingrese opción a ejecutar: "))
			if (opc == 1):
				self.menu_usuarios()
			elif (opc == 2):
				self.menu_sistema()
			elif (opc == 3):
				print("Gracias por utilizar el sistema. Usted ha salida correctamente!")

	def menu_usuarios(self):
		print("\n---------- Menu Usuarios -----------------")
		print("1.- Agregar usuarios")
		print("2.- Eliminar usuarios\n")
		sel = int(input("Ingrese opción a ejecutar: "))
		if (sel == 1):
			print("Inserte la informacion que se le pedi acontinuacion\n")
			usuario = input("Ingrese usuario a agregar: ")
			if self.__LU.buscar(usuario)==False:
				password = input ("Ingrese password: ")
				print(self.__LU.agregar(usuario, password))
			else:
				print("\nEl nombre de usuario ya existe intente nuevamente con uno diferente\n")
		elif (sel == 2):
			print("Inserte la informacion que se le pedi acontinuacion\n")
			usuario = input("Ingrese usuario a eliminar: ")
			if self.__LU.eliminar(usuario)==True:
				print("\nEl usuario eliminado correctamente\n")
			else:
				print("\nEl usuario no se pudo eliminar\n")
	def menu_sistema(self):

		if(self.__logeado == True):
			sel = 0
			while (sel != 6):
				print("\n---------- Menu Sistema -----------------")
				print("1.- Leer Archivo")
				print("2.- Resolver Operaciones")
				print("3.- Operar Matriz")
				print("4.- Mostrar Usuarios")
				print("5.- Mostrar Cola")
				print("6.- Cerrar Sesion\n")
				sel = int(input("Ingrese opción a ejecutar: "))
				if (sel == 1):
					ruta = input("\nIngrese ruta del archivo: ")
					Ar = A.LeerArchivo(ruta)
					us = self.__LU.buscarE(self.__nick)
					us.Cola = Ar.obtenerCola()
					if (us.Archivo == False):
						us.Archivo = True
						us.crearMatriz(Ar.dimX, Ar.dimY)
					self.__log = us

				elif (sel == 2):
					if (self.__log!= None and self.__log.Archivo == True):
						self.menuOperaciones()
					else:
						print("Debe cargar un archivo primero")
				elif (sel == 3):
					if (self.__log!= None and self.__log.Archivo == True):
						self.menuOperaciones()
					else:
						print("Debe cargar un archivo primero")
				elif (sel == 4):
					self.__LU.imprimirInicio()
					self.__LU.imprimirFin()
				elif (sel == 5):
					if (self.__log!= None and self.__log.Archivo == True):
						self.__log.Cola.show()
					else:
						print("Debe cargar un archivo primero")
					
				elif (sel == 6):
					self.__logeado = False
					self.__nick = ""
		else:
			print("Usted no se encuentra logeado favor ingresar datos\n")
			usuario = input("Usuario: ")
			password = input ("Pass: ")
			self.__logeado = self.__LU.login(usuario,password)
			if self.__logeado == True:
				print("Ya puede ingresar al menu de la opcion 2\n")
				self.__nick = usuario

	def menuOperaciones(self):
		opc = 0
		while (opc != 2):
			print("\n-------------- Menu Operaciones --------------")
			print("1.- Resolver Operaciones")
			print("2.- Regresar\n")
			opc = int(input("Ingrese opción a ejecutar: "))
			if (opc == 1):
				try:
					ops = self.__log.Cola.dequeue()
					if(ops == None):
						print("La cola esta vacia")
					else:
						lis = ops.split(" ")
						pila = P.Pila()
						for el in lis:
							pila.push(P.EPila(el))
							if(el == "+"):
								pila.pop()
								num1 = pila.pop()
								num2 = pila.pop()
								re = int(num1)+int(num2)
								pila.push(P.EPila(str(re)))
								print(num2 + " + " +num1 +" = "+ str(re))
							elif (el == "-"):
								pila.pop()
								num1 = pila.pop()
								num2 = pila.pop()
								re = int(num1)-int(num2)
								pila.push(P.EPila(str(re)))
								print(num2 + " - " +num1 +" = "+ str(re))
							elif (el == "*"):
								pila.pop()
								num1 = pila.pop()
								num2 = pila.pop()
								re = int(num1)*int(num2)
								pila.push(P.EPila(str(re)))
								print(num2 + " * " +num1 +" = "+ str(re))
				except:
				 	print("No fue posible operar")