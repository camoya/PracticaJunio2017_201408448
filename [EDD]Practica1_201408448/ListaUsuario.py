import Usuario
U = Usuario
class ListaUsuario:
	""" lista de usuario aca irian las funciones de la lista"""
	def __init__(self):
		self.__inicio = None
		self.__fin = None

	def agregar(self, user, passw):
		userAdd = U.Usuario(user,passw)
		if self.__inicio == None:
			self.__inicio = self.__fin = userAdd
			self.__fin.set_sig(self.__inicio)
			self.__inicio.set_ant(self.__fin)	
			return "Agregado correctamente"
		else:
			self.__fin.set_sig(userAdd)
			userAdd.set_ant(self.__fin) 
			self.__fin = userAdd
			self.__fin.set_sig(self.__inicio)
			return "Agregado correctamente"
		return "No se ha logrado insertar"

	def buscar(self, user):
		valido = False
		temp = self.__inicio
		while (temp != None):
			if temp.get_user() == user:
				valido = True
			if temp == self.__inicio:
				temp = None
			else:
				temp= temp.get_sig
		return valido

	def buscarE (self, user):
		temp = self.__inicio
		while (temp != None):
			if temp.get_user() == user:
				return temp
			if temp == self.__inicio:
				temp = None
			else:
				temp= temp.get_sig
		return False

	def login(self, user, passw):
		valido = False
		temp = self.__inicio
		while (temp != None):
			if temp.get_user() == user and temp.get_pass() == passw:
				valido = True
			if temp == self.__inicio:
				temp = None
			else:
				temp= temp.get_sig
		if valido == False:
			print ("Credenciales incorrectas\n")
		else:
			print ("Usted a iniciado sesión correctamente\n")
		return valido
	def imprimirInicio(self):
		if self.__inicio == None:
			print ("Lista de usuarios vacia")
		else :
			temp = self.__inicio
			while (temp is not None):
				print (temp.get_user())
				if temp == self.__inicio:
					temp = None
				else:
					temp= temp.get_sig

	def imprimirFin(self):
		if self.__inicio  is None:
			print ("Lista de usuarios vacia")
		else :

			temp = self.__fin	
			while (temp is not None):
				print (temp.get_user())
				if temp == self.__fin:
					temp = None
				else:
					temp= temp.get_ant
				