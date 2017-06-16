import os
import xml.etree.ElementTree
import Cola
C = Cola
class LeerArchivo():
	def __init__(self, url):
		self.__url = url
		self.dimX = 0
		self.dimY = 0
		self.__listaOpe = C.Cola()

	def obtenerCola(self):
		e = xml.etree.ElementTree.parse(self.__url).getroot()
		opers = e.find('operaciones')
		mat = e.find('matriz')
		dimX = mat.find('x').text
		dimY = mat.find('y').text
		for atype in opers.findall('operacion'):
			ele = C.ECola(atype.text)
			self.__listaOpe.enqueue(ele)
		return self.__listaOpe
		
        
"""doc = etree.parse(str(self.__url))
		raiz = doc.getroot()
		libro = raiz[0]
		for child in raiz:
			#print child.tag
			if child.tag == 'matriz':				
				for child2 in child:
					#print child2.tag
					if child2.tag == 'x':
						self.dimX = int(child2.text)
					elif child2.tag == 'y':
						self.dimY = int(child2.text)
			elif child.tag == 'operaciones':
				for child2 in child:
					if child2.tag == 'operacion':
						ele = C.ECola(child2.text)
						self.__listaOpe.enqueue(ele)
		return self.__listaOpe"""
