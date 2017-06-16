class IU:
	def __init__(self):
		self.__logeado=False

	def menu_general():
		opc = 0
		while (opc != 3):
			print("Cristhofer Alexander Moya Contreras - 201408448")
			print("Practica 1 [EDD] Junio 2017\n")
			print("1.- Crear usuario")
			print("2.- Ingresar al sistema")
			print("3.- Salir del sistema\n")
			opc = int(input("Ingrese opción a ejecutar: "))
			if (opc == 1):
				menu_usuarios()
			elif (opc == 2):
				menu_sistema()
			else:
				print("Gracias por utilizar el sistema. Usted ha salida correctamente!")

	def menu_usuarios():
		print("\n1.- Agregar usuarios")
		print("2.- Eliminar usuarios")
		print("3.- Buscar usuarios")
		sel = int(input("Ingrese opción a ejecutar: "))

	def menu_sistema():
		if(logeado == True):
			print("Opciones disponigles")
		else:
			print("Usted no se encuentra logeado favor ingresar datos\n")
			usuario = input("Usuario: ")
			password = input ("Pass: ")

