class Semantico():
	def __init__(self,arbol):
		self._arbol = arbol
		self.funcTable = []
		self.varTable = []
		self.errores = []
		self.ambito = "global"


	def createTables(self):
		for item in self._arbol:
			if(item.name=='DefFunc'):
				self.funcTable.append([item.list[0],item.list[1]])
				self.ambito = item.list[1]
			if(item.name=='definicion'):
				self.ambito = "global"
			if(item.name=='DefVar'):
				self.varTable.append([item.list[0],item.list[1],self.ambito])
			if(item.name=='Parametros' and len(item.list)>0):
				self.varTable.append([item.list[0],item.list[1],self.ambito])
			if(item.name=='ListaParam' and len(item.list)>0):
				self.varTable.append([item.list[1],item.list[2],self.ambito])

		print('\n\n')
		print('============= Tablas ===============')
		print('Tabla de Funciones')
		for item in self.funcTable:
			print(item)
		print('\n')
		print('Tabla de Variables')
		for item in self.varTable:
			print(item)

	def checkErrors(self):
		valores = []
		self.ambito = "global"
		for item in self.funcTable:
			if item[1] in valores:
				self.errores.append('La funcion <'+item[1]+'> ha sido duplicada')
			else:
				valores.append(item[1])

		valores = []
		for item in self.varTable:
			if item in valores:
				self.errores.append('La variable <'+item[1]+'> ya existe en el ambito <'+item[2]+'>')
			else:
				valores.append(item)

		for item in self._arbol:
			if(item.name=='DefFunc'):
				self.ambito = item.list[1]
			if(item.name=='definicion'):
				self.ambito = "global"


			if item.name == 'Sentencia' or item.name == 'Termino':
				existe = False
				var = item.list[0]
				for lista in self.varTable:
					if (var in lista and (lista[2]==self.ambito or lista[2]=='global')) or var.isdigit():
						existe = True

				if not existe:
					self.errores.append('No existe la variable <'+var+'>')


		print('\n\n')
		print('============= Errores ===============')
		print(self.errores)




		











