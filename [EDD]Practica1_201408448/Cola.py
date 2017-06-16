class ECola(object):
	""" Elemento o nodo de la cola"""
	def __init__(self, valor):
		self.valor = valor
		self.sig = None

class Cola(object):
	"""Lista de EPila"""
	def __init__(self):
		self.__inicio = None

	def enqueue(self, elemento):
		if self.__inicio == None:
			self.__inicio = elemento
		else:
			temp = self.__inicio
			while temp.sig != None:	
				temp = temp.sig

			temp.sig = elemento

	def dequeue(self):
		if self.__inicio.sig == None:
			val = self.__inicio.valor
			self.__inicio = None
			return val
		else :
			val = self.__inicio.valor
			self.__inicio = self.__inicio.sig
			return val

	def show(self):
		temp = self.__inicio
		cnt = 0
		while temp!= None:
			print("\nindice "+ str(cnt)+ ": "+str(temp.valor))
			cnt = cnt +1
			temp = temp.sig