import sys

class maquinaVirtual:

	dirPrincipal = None

	InstruccionIndex = 0

	cuadruplos = None

	memoria = [[[],[],[]],[[],[],[]]]

	stackCantidadEspacio = []  #cada elemento [Int, decimal , texto]

	stackPorReferenciaFunciones = [] #cada elemento[[direccion, direccion], ...]

	stackDireccionesFunciones = []

	stackRetornos = []

	contLocalInt = 0

	contLocalDecimal = 0

	contLocalTexto = 0
	def __init__(self, dirPrincipal:dict, cuadruplos:list, contGlobalInt:int, contGlobalDecimal:int, contGlobalTexto:int, contInicioInt:int, contInicioDecimal:int, contInicioTexto:int):
		self.dirPrincipal = dirPrincipal
		self.cuadruplos = cuadruplos
		self.memoria[0][0] = [0] * contGlobalInt
		self.memoria[0][1] = [0.0] * contGlobalDecimal
		self.memoria[0][2] = [""] * contGlobalTexto
		self.memoria[1][0] = [0] * contInicioInt
		self.memoria[1][1] = [0.0] * contInicioDecimal
		self.memoria[1][2] = [""] * contInicioTexto
		self.contLocalInt = contInicioInt
		self.contLocalDecimal = contInicioDecimal
		self.contLocalTexto = contInicioTexto
		self.stackCantidadEspacio.append([contInicioInt,contInicioDecimal, contInicioTexto])

	def obtenerDireccion(self, direccion:int):
		indexs = [0, 0, 0]
		if direccion >= 9000:
			indexs[0] = 1
			if direccion >= 9000 and direccion < 15000:
				indexs[1] = 0
				indexs[2] = direccion - 9000 - self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 1][0] + self.contLocalInt
				return indexs
			elif direccion >= 15000 and direccion < 21000:
				indexs[1] = 1
				indexs[2] = direccion - 15000 - self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 1][1] + self.contLocalDecimal
				return indexs
			elif direccion >= 21000 and direccion < 27000:
				indexs[1] = 2
				indexs[2] = direccion - 21000 - self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 1][2] + self.contLocalTexto
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
			while True:
				try:
					self.memoria[indexs[0]][indexs[1]][indexs[2]] = int(input('Escribe tu entrada:'))
					break
				except ValueError:
					print("Numero Invalido, Intente nuevamente")
		elif indexs[1] == 1:
			while True:
				try:
					self.memoria[indexs[0]][indexs[1]][indexs[2]] = float(input('Escribe tu entrada:'))
					break
				except ValueError:
					print("Numero invalido, Intente nuevamente")
		elif indexs[1] == 2:
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = input('Escribe tu entrada:')

	def gotof(self):
		indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][1])
		if self.memoria[indexs[0]][indexs[1]][indexs[2]] == 0:
			self.InstruccionIndex = self.cuadruplos[self.InstruccionIndex][3] - 1

	def asignar(self):
		aux1 = None
		if type(self.cuadruplos[self.InstruccionIndex][1]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][1])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][1]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][1][0]	

		indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
		if indexs[1] == 0:
			try:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = int(aux1)
			except ValueError:
				print("Numero invalido, no se pudo completar la asignacion")
		elif indexs[1] == 1:
			try:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = float(aux1)
			except ValueError:
				print("Numero invalido, no se pudo completar la asignacion")
		else:
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = str(aux1)

	def era(self):
		self.stackPorReferenciaFunciones.append([])
		aux = self.cuadruplos[self.InstruccionIndex][3]
		self.stackCantidadEspacio.append(aux)
		self.memoria[1][0] = self.memoria[1][0] + ([0] * aux[0])
		self.contLocalInt = self.contLocalInt + aux[0]
		self.memoria[1][1] = self.memoria[1][1] + ([0.0] * aux[1])
		self.contLocalDecimal = self.contLocalDecimal + aux[1]
		self.memoria[1][2] = self.memoria[1][2] + ([""] * aux[2])
		self.contLocalTexto = self.contLocalTexto + aux[2]

	def gosub(self):
		self.stackDireccionesFunciones.append(self.InstruccionIndex)
		self.InstruccionIndex = self.cuadruplos[self.InstruccionIndex][3] - 1

	def param(self):
		aux = self.cuadruplos[self.InstruccionIndex]
		valor = None
		if type(aux[3]) is int:
			indexs = self.obtenerDireccion(aux[3])
			valor = self.memoria[indexs[0]][indexs[1]][indexs[2] - self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 2][indexs[1]]
			]

		elif type(aux[3]) is list:
			valor = aux[3][0]

		indexs = self.obtenerDireccion(aux[2])
		self.memoria[indexs[0]][indexs[1]][indexs[2]] = valor
		if aux[1]:
			self.stackPorReferenciaFunciones[len(self.stackPorReferenciaFunciones) - 1].append([aux[2], aux[3]])

	def asignarReferencias(self, referencias:list):
		for par in referencias:
			indexs1 = self.obtenerDireccion(par[0])
			indexs2 = self.obtenerDireccion(par[1])
			self.memoria[indexs2[0]][indexs2[1]][indexs2[2]- self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 2][indexs2[1]]] = self.memoria[indexs1[0]][indexs1[1]][indexs1[2]]

	def endproc(self):
		self.InstruccionIndex = self.stackDireccionesFunciones.pop()
		referencias = self.stackPorReferenciaFunciones.pop()
		self.asignarReferencias(referencias)
		aux = self.stackCantidadEspacio.pop()
		if aux[0] > 0:
			del self.memoria[1][0][-aux[0]:]
			self.contLocalInt = self.contLocalInt - aux[0]
		if aux[1] > 0:
			del self.memoria[1][1][-aux[1]:]
			self.contLocalDecimal = self.contLocalDecimal - aux[1]
		if aux[2] > 0:
			del self.memoria[1][2][-aux[2]:]
			self.contLocalTexto = self.contLocalTexto - aux[2]

	def retornar(self):
		aux1 = None
		if type(self.cuadruplos[self.InstruccionIndex][3]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][3]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][3][0]
		print (aux1)
		if len(self.stackRetornos) > 0:	
			indexs2 = self.obtenerDireccion(self.stackRetornos.pop())
			print(indexs2)
			self.memoria[indexs2[0]][indexs2[1]][indexs2[2]- self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 2][indexs2[1]]] = aux1

	def guardarDirRetornar(self):
		print("hola")
		self.stackRetornos.append(self.cuadruplos[self.InstruccionIndex][3])
#ERA, null, null, [contEnteros,contDecimales,contTextos]

#PARAM, true/false referencia, DirFuncionLocal, DirLLamada/[constante]

#Retornar: =, valor/dir, None, DirDestino

#GOSUB,null,null,direccionInicioFuncion

#[ENDPROC, None, None, None]

#[END, None, None, None]

#[RETORNAR,direccionqueManda,None,direccionDestino]

	def empezar(self):
		while (self.cuadruplos[self.InstruccionIndex][0] != "END"):
			if self.cuadruplos[self.InstruccionIndex][0] in ["+", "-", "*", "/", "==", ">", "&&", "||", "<", "!=", ">=", "<="]:
				self.operacionBasica(self.cuadruplos[self.InstruccionIndex][0])

			elif self.cuadruplos[self.InstruccionIndex][0] == "goto":
				self.InstruccionIndex = self.cuadruplos[self.InstruccionIndex][3] - 1

			elif self.cuadruplos[self.InstruccionIndex][0] == "=":
				self.asignar()

			elif self.cuadruplos[self.InstruccionIndex][0] == "ENDPROC":
				self.endproc()

			elif self.cuadruplos[self.InstruccionIndex][0] == "ERA":
				self.era()

			elif self.cuadruplos[self.InstruccionIndex][0] == "PARAM":
				self.param()

			elif self.cuadruplos[self.InstruccionIndex][0] == "gotof":
				self.gotof()

			elif self.cuadruplos[self.InstruccionIndex][0] == "GOSUB":
				self.gosub()

			elif self.cuadruplos[self.InstruccionIndex][0] == "escribir":
				self.escribir()

			elif self.cuadruplos[self.InstruccionIndex][0] == "leer":
				self.leer()
			elif self.cuadruplos[self.InstruccionIndex][0] == "RETORNAR":
				self.retornar()
			elif self.cuadruplos[self.InstruccionIndex][0] == "asignacionRetorno":
				self.guardarDirRetornar()
			self.InstruccionIndex = self.InstruccionIndex + 1


