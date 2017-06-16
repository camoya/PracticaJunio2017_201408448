import Matriz
M = Matriz
class Usuario:
	"""Nodo tipo usuario"""
	def __init__(self, username, password):
		self.__username = username
		self.__password = password
		self.__sig = None
		self.__ant = None
		self.__matriz = M.Matriz(None, None, None, None)
		self.__trans = M.Matriz(None, None, None, None)
		self.__TamX = 0
		self.__TamY = 0
		self.__Archivo=False

	def get_user(self):
		return self.__username
	def set_user(self, name):
		self.__username = name
	def get_pass(self):
		return self.__password
	def set_pass(self, pas):
		self.__password = pas
	def set_sig(self, siguiente):
		self.__sig = siguiente
	def get_sig(self):
		return self.__sig
	def set_ant(self, anterior):
		self.__ant = anterior
	def get_ant(self):
		return self.__ant

	def crearMatriz(self, dim1, dim2):
		self.__TamX = dim1
		self.__TamY = dim2
		casEx = self.__matriz
		for x in range(0, dim1+1):
			for y in range(0, dim2+1):
				cas = casEx
				if x == 0 and y != 0:
					casNueva =  M.Matriz(None, cas, None, None)
					cas.posmY = casNueva
					cas = casNueva
				elif x != 0:
					casNueva =  M.Matriz(None, cas, cas.posmX.posmY, None)
					cas.posmY = casNueva
					cas.posmX.posmY.posX= casNueva
					cas = casNueva
			if x != dim1:
				casNuevaX = M.Matriz(None, None, casEx, None)
				casEx.posX = casNuevaX
				casEx = casNuevaX

	def crearTranspuesta(self):
		dim1 = self.__TamY
		dim1 = self.__TamX
		casEx = self.__trans
		for x in range(0, dim1+1):
			for y in range(0, dim2+1):
				cas = casEx
				if x == 0 and y != 0:
					casNueva =  M.Matriz(None, cas, None, None)
					casNueva.set_valor = self.buscarCasilla(y,x)
					cas.posmY = casNueva
					cas = casNueva
				elif x != 0:
					casNueva =  M.Matriz(None, cas, cas.posmX.posmY, None)
					casNueva.set_valor = self.buscarCasilla(y,x).get_valor
					cas.posmY = casNueva
					cas.posmX.posmY.posX= casNueva
					cas = casNueva
			if x != dim1:
				casNuevaX = M.Matriz(None, None, casEx, None)
				casNuevaX.set_valor = self.buscarCasilla(0,x).get_valor
				casEx.posX = casNuevaX
				casEx = casNuevaX			

				

	def buscarCasilla(self, posX, posY):
		cas = self.Matriz
		for x in range(0, posX+1):
			cas = cas.posX
		for y in range(0, posY+1):
				cas = cas.posmY	
		return cas