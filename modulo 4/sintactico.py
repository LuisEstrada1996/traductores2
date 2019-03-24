import os
from lexico import Lexico
from pila import Pila
import matriz as mat
os.system('clear')


matriz = mat.matriz 
valores = mat.valores
reglas = mat.reglas

class Sintactico():
	def __init__(self,size):
		self.pila = Pila()
		self.pila.push('$')
		self.pila.push('0')
		self.columna = 0
		self.cantidad = size
		self.accion = ""
		self.arbol = {}
		self.list_tmp = list()
		
	def comparar(self,token):
		if(valores[token]):
			self.accion = matriz[int(self.pila.top())][int(valores[token])]
			print('Pila: ', self.pila.get())
			print('Token: ', token)
			if(self.accion == -1):
				print('Cadena valida')
				print(self.arbol)
				exit()
			elif(self.accion > 0):
				self.pila.push(self.accion)
				self.list_tmp.append('')
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
				self.arbol.update({reglas[self.accion]['nombre']: ''})
				if(reglas[self.accion]['cantidad'] > 0):
					print('Lista:' ,self.list_tmp)
					aux = reglas[self.accion]['cantidad']
					list_aux = []
					for i in range(aux):
						valor = self.list_tmp.pop(-1)
						if(valor !=''):
							print(valor)
							list_aux.append(valor)

					self.arbol[reglas[self.accion]['nombre']] = list_aux
				self.list_tmp.append(reglas[self.accion]['nombre'])



				self.comparar(token)
				


				
			else: 
				print('Invalida')
				exit()
			

	
			
cadena = input('Ingresar cadena: ')
lexico = Lexico(cadena)
tokens = list()
while(lexico.termino() == False):
  lexico.sigPosicion()
  if(lexico.boolToken):
    tokens.append(lexico.token)
    lexico.boolToken = False

lexico.tipoDato(lexico.state)
tokens.append(lexico.token)
tokens.append('$')



sintactico = Sintactico(len(tokens)-1)
i = 0
for token in tokens:
	sintactico.comparar(token)
	i+=1











