import sys

class maquinaVirtual:

	dirPrincipal = None

	InstruccionIndex = 0

	cuadruplos = None

	memoria = [[[],[],[]],[[],[],[]]]

	stackComienzoFunciones = []

	def __init__(self, dirPrincipal:dict, cuadruplos:list, contGlobalInt:int, contGlobalDecimal:int, contGlobalTexto:int):
		self.dirPrincipal = dirPrincipal
		self.cuadruplos = cuadruplos
		self.memoria[0][0] = [0] * contGlobalInt
		self.memoria[0][1] = [0.0] * contGlobalDecimal
		self.memoria[0][2] = [""] * contGlobalTexto

	def obtenerDireccion(self, direccion:int):
		indexs = [0, 0, 0]
		if direccion >= 9000:
			indexs[0] = 1
			if direccion >= 9000 and direccion < 15000:
				indexs[1] = 0
				indexs[2] = direccion - 9000 + self.stackComienzoFunciones[len(stackComienzoFunciones) - 1][0]
				return indexs
			elif direccion >= 15000 and direccion < 21000:
				indexs[1] = 1
				indexs[2] = direccion - 15000 + self.stackComienzoFunciones[len(stackComienzoFunciones) - 1][1]
				return indexs
			elif direccion >= 21000 and direccion < 27000:
				indexs[1] = 2
				indexs[2] = direccion - 21000 + self.stackComienzoFunciones[len(stackComienzoFunciones) - 1][2]
				return indexs
		else:
			if direccion < 3000:
				indexs[1] = 0
				indexs[2] = direccion
				return indexs
			elif direccion >= 3000 and direccion < 6000:
				indexs[1] = 1
				indexs[2] = direccion - 3000
				return indexs
			elif direccion >= 6000 and direccion < 9000:
				indexs[1] = 2
				indexs[2] = direccion - 6000
				return indexs

	def operacionBasica(self, op:str):
		aux1 = 0
		aux2 = 0
		if type(self.cuadruplos[self.InstruccionIndex][1]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][1])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][1]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][1][0]

		if type(self.cuadruplos[self.InstruccionIndex][2]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][2])
			aux2 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][2]) is list:
			aux2 = self.cuadruplos[self.InstruccionIndex][2][0]

		indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
		if op == "+":
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = aux1 + aux2
		elif op == "*":
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = aux1 * aux2
		elif op == "/":
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = aux1 / aux2
		elif op == "-":
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = aux1 - aux2
		elif op == "==":
			if aux1 == aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == ">":
			if aux1 > aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "&&":
			if aux1 and aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "||":
			if aux1 or aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "<":
			if aux1 < aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "!=":
			if aux1 != aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == ">=":
			if aux1 >= aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "<=":
			if aux1 <= aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0

	def escribir(self):
		aux1 = None
		if type(self.cuadruplos[self.InstruccionIndex][3]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][3]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][3][0]
		print(aux1)

	def leer(self):
		indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
		if indexs[1] == 0:
			try:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = int(input('Escribe tu entrada:'))
			except ValueError:
				print("Numero Invalido")
		elif indexs[1] == 1:
			try:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = float(input('Escribe tu entrada:'))
			except ValueError:
				print("Numero invalido")
		elif indexs[1] == 2:
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = input('Escribe tu entrada:')

	def empezar(self):
		while (self.cuadruplos[self.InstruccionIndex[0]] != "END"):
			if self.cuadruplos[self.InstruccionIndex][0] in ["+", "-", "*", "/", "==", ">", "&&", "||", "<", "!=", ">=", "<="]:
				self.operacionBasica(self.cuadruplos[self.InstruccionIndex][0])

			#elif self.cuadruplos[self.InstruccionIndex][0] == "goto":

			#elif self.cuadruplos[self.InstruccionIndex][0] == "ENDPROC":

			#elif self.cuadruplos[self.InstruccionIndex][0] == "ERA":

			#elif self.cuadruplos[self.InstruccionIndex][0] == "PARAM":

			#elif self.cuadruplos[self.InstruccionIndex][0] == "gotof":

			#elif self.cuadruplos[self.InstruccionIndex][0] == "GOSUB":

			elif self.cuadruplos[self.InstruccionIndex][0] == "escribir":
				self.escribir()

			elif self.cuadruplos[self.InstruccionIndex][0] == "leer":
				self.leer()

			self.InstruccionIndex = self.InstruccionIndex + 1




			
		