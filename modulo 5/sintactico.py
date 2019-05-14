import os
from pila import Pila
import matriz as mat
os.system('clear')

matriz = mat.matriz 
valores = mat.valores
reglas = mat.reglas

class nodo():
	def __init__(self, name, regla, lista):
		self.name = name
		self.regla = regla
		self.list = lista

class Sintactico():
	def __init__(self,size):
		self.pila = Pila()
		self.pila.push('$')
		self.pila.push('0')
		self.columna = 0
		self.cantidad = size
		self.accion = ""
		self.list_tmp = list()
		self.arbol = []
		
	def comparar(self,token,valor):
		if(valores[token]):
			self.accion = matriz[int(self.pila.top())][int(valores[token])]
			print('Pila: ', self.pila.get())
			print('Token: ', token)
			if(self.accion == -1):
				print('Cadena valida\n')
				print('==== Arbol ====')
				self.arbol = self.arbol[::-1]
				for item in self.arbol:
					item.list = item.list[::-1]
					print(item.regla,'==> ',item.list)


			elif(self.accion > 0):
				self.pila.push(self.accion)
				self.list_tmp.append(valor)
				print('Accion: PUSH')
				print('\n')

			elif(self.accion < 0):
				self.pila.pop(reglas[self.accion]['cantidad'])
				self.pila.push(matriz[int(self.pila.top())][reglas[self.accion]['columna']])
				print('-----GENERA REGLA-----')
				print('Accion: POP %d elementos'%reglas[self.accion]['cantidad'])
				print('Accion: PUSH de la regla')
				print('Nombre: ', reglas[self.accion]['nombre'])
				print('\n')

				list_aux = []
				if(reglas[self.accion]['cantidad'] > 0):
					print('Lista:' ,self.list_tmp)
					aux = reglas[self.accion]['cantidad']
					for i in range(aux):
						valor2 = self.list_tmp.pop(-1)
						list_aux.append(valor2)

				self.arbol.append(nodo(reglas[self.accion]['nombre'], reglas[self.accion]['regla'], list_aux))
				self.list_tmp.append(reglas[self.accion]['regla'])
				self.comparar(token,valor)

			else: 
				print('Invalida')
				exit()
			

	
		











