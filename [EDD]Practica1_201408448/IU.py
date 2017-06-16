import ListaUsuario
LU = ListaUsuario
class IU:
	def __init__(self):
		self.__logeado=False
		self.__nick =""
		self.__LU = LU.ListaUsuario()
	def menuGeneral(self):
		opc = 0
		while (opc != 3):
			print("\n-------------- Menu Principal --------------")
			print("Cristhofer Alexander Moya Contreras - 201408448")
			print("Practica 1 [EDD] Junio 2017\n")
			print("1.- Crear usuario")
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
		print("2.- Eliminar usuarios")
		print("3.- Buscar usuarios\n")
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
			self.menu_sistema()
		elif (sel == 3):
			print("Gracias por utilizar el sistema. Usted ha salida correctamente!")
	def menu_sistema(self):

		if(self.__logeado == True):
			sel = 0
			while (sel != 6):
				print("\n---------- Menu Sistema -----------------")
				print("1.- Leer Archivo")
				print("2.- Resolver Operaciones")
				print("3.- Operar Matriz")
				print("4.- Mostrar Usuario")
				print("5.- Mostrar Cola")
				print("6.- Cerrar Sesion\n")
				sel = int(input("Ingrese opción a ejecutar: "))
				if (sel == 1):
					ruta = input("\nIngrese ruta del archivo: ")
					
				elif (sel == 2):
					self.menu_sistema()
				elif (sel == 3):
					print("Gracias por utilizar el sistema. Usted ha salida correctamente!")
				elif (sel == 4):
					self.menu_sistema()
				elif (sel == 5):
					self.menu_sistema()
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

