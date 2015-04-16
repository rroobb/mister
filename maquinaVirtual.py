import sys
from cubo_semantico import *

class maquinaVirtual:

	dirPrincipal = None

	cuboSem = cubo_semantico()

	InstruccionIndex = 0

	cuadruplos = None

	memoria = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]


	def __init__(self, dirPrincipal:dict, cuadruplos:list):
		self.dirPrincipal = dirPrincipal
		self.cuadruplos = cuadruplos

	#def empezar(self):
		#while self.cuadruplos[self.InstruccionIndex[0]] != "END":