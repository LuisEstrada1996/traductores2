class Semantico():
	def __init__(self,arbol):
		self._arbol = arbol
		self.funcTable = []
		self.varTable = []
		self.errores = []
		self.ambito = "global"
		self.actual = ""
		self.opActual = ""
		self.cantidad = 0
		self.code = ""


	def createTables(self):
		for item in self._arbol:
			if(item.name=='DefFunc'):
				self.funcTable.append([item.list[0],item.list[1]])
				self.ambito = item.list[1]
			if(item.name=='definicion'):
				self.ambito = "global"
			if(item.name=='DefVar'):
				self.varTable.append([item.list[0],item.list[1],self.ambito, ''])
			if(item.name=='Parametros' and len(item.list)>0):
				self.varTable.append([item.list[0],item.list[1],self.ambito, ''])
			if(item.name=='ListaParam' and len(item.list)>0):
				self.varTable.append([item.list[1],item.list[2],self.ambito, ''])
			




		

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


			if(item.name=='Sentencia' and len(item.list)>1):
				self.actual = item.list[0]

			if(item.name=='Expresion' and len(item.list)>1):
				self.opActual = item.list[1]


			if(item.name=='Termino'):
				var = item.list[0]
				for lista in self.varTable:
					if self.actual == lista[1]:
						lista[3] += var
						if(self.opActual):
							lista[3] += self.opActual
				self.opActual = ""

				

			
		print('\n\n')
		print('============= Tablas ===============')
		print('Tabla de Funciones')
		for item in self.funcTable:
			print(item)
		print('\n')
		print('Tabla de Variables')
		for item in self.varTable:
			print(item)
				
		print('\n\n')
		print('============= Errores ===============')
		print(self.errores)

		self.code = "section .data\n"
		for item in self.varTable:
			aux = item[3].find('+')
			if aux==-1:
				self.code += item[1]+" dq '"+item[3]+"'\n"
			else:
				self.code += item[1]+" dq '0'\n"

		self.code += "section .text\nglobal _start\n_start:\n"
		for item in self.varTable:
			aux = item[3].find('+')
			if aux>-1:
				aux = item[3].split('+')
				self.code += "mov eax,["+item[1]+"]\n"
				self.code += "sub eax,'0'\n"
				self.code += "mov ebx,["+aux[0]+"]\n"
				self.code += "sub ebx,'0'\n"
				self.code += "add eax,ebx\n"
				self.code += "add eax,'0'\n"
				self.code += "mov ["+item[1]+"],eax\n"
				self.code += "mov eax,["+item[1]+"]\n"
				self.code += "sub eax,'0'\n"
				self.code += "mov ebx,["+aux[1]+"]\n"
				self.code += "sub ebx,'0'\n"
				self.code += "add eax,ebx\n"
				self.code += "add eax, '0'\n"
				self.code += "mov ["+item[1]+"], eax\n"
				self.code += "mov ecx, "+item[1]+"\n"
				self.code += "mov edx, 1\n"
				self.code += "mov ebx, 1\n"
				self.code += "mov eax, 4\n"

		self.code += "int 0x80\nmov eax,1\nint 0x80"

		print('\n\n')
		print('============= Ensamblador ===============')
		print(self.code)






		











