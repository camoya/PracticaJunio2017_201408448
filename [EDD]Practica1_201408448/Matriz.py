class Matriz:
	def __init__(self, posX, posY, posmX, posmY):
		self.posX = posX
		self.posY = posY
		self.posmX = posmX
		self.posmY = posmY
		self.__valor = None

	def set_valor(self, val):
		self.__valor = val
		
	def get_valor(self):
		return self.__valor