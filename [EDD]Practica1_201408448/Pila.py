
class EPila():
	""" Elemento o nodo de la pila"""
	def __init__(self, valor):
		self.valor=valor
		self.sig=None

class Pila():
	"""Lista de EPila"""
	def __init__(self):
		self.__primero= None

	def push(self, elemento):
		if self.__primero == None:
			self.__primero = elemento
		else:
			elemento.sig=self.__primero
			self.__primero = elemento

	def pop(self):
		dato = self.__primero.valor
		self.__primero = self.__primero.sig
		return dato

	def show(self):
		temp = self.__primero
		cadena = ''
		while temp!= None:
			cadena = str(cadena) + str (temp.valor) + ' '
			temp = temp.siguiente
		print(cadena)