import os
from lexico import Lexico
from pila import Pila
os.system('clear')

"""
matriz = ([2, 0, 0, 1],
		  [0, 0,-1, 0],
		  [0, 3, -3, 0],
		  [2, 0, 0, 4],
		  [0, 0, -2, 0])
"""

valores = {'ID':'0', 'PLUS': 1, '$': 2}
reglas = {
		   -2: {'nombre': 'E','columna':3,'cantidad':3},
		   -3: {'nombre': 'E','columna':3,'cantidad':1}
		 };

class Sintactico():
	def __init__(self,size):
		self.pila = Pila()
		self.pila.push('$')
		self.pila.push('0')
		self.columna = 0
		self.cantidad = size
		self.accion = ""
		
	def comparar(self,token):
		if(valores[token]):
			self.accion = matriz[int(self.pila.top())][int(valores[token])]
			if(self.accion == -1):
				print('Cadena valida')
			elif(self.accion > 0):
				self.pila.push(self.accion)
			elif(self.accion < 0):
				self.pila.pop(reglas[self.accion]['cantidad'])
				self.pila.push(matriz[int(self.pila.top())][reglas[self.accion]['columna']])
				self.comparar('$')
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
for token in tokens:
	sintactico.comparar(token)











