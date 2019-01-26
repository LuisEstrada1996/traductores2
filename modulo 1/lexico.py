import os
os.system('clear')

class Lexico():
  def __init__(self, string):
    self.state = 0
    self.string = string
    self.pos = -1
    self.valid = True
    self.size = len(string)

  def asignarEstado(self, c):
    #Estado 0
    if self.state == 0:
      if c.isdigit() and int(c) >= 0:
        self.state = 1
        self.sigPosicion()
      elif c == '|':
        self.state = 4
        self.sigPosicion()
      elif c == '&':
        self.state = 6
        self.sigPosicion()
      elif c == '*':
        self.state = 8
        self.sigPosicion()
      elif c == '/':
        self.state = 9
        self.sigPosicion()
      elif c == '=':
        self.state = 10
        self.sigPosicion()
      elif c == '<':
        self.state = 12
        self.sigPosicion()
      elif c == '>':
        self.state = 14
        self.sigPosicion()
      elif c == '!':
        self.state = 16
        self.sigPosicion()
      elif c == '(':
        self.state = 18
        self.sigPosicion()
      elif c == ')':
        self.state = 19
        self.sigPosicion()
      elif c == '{':
        self.state = 20
        self.sigPosicion()
      elif c == '}':
        self.state = 21
        self.sigPosicion()
      elif c == ';':
        self.state = 22
        self.sigPosicion()
      elif c == '+':
        self.state = 23
        self.sigPosicion()
      elif c == '-':
        self.state = 24
        self.sigPosicion()

      else: 
        self.tipoDato(-1)

    #Estado 1
    elif self.state == 1:
      if c == '.':
        self.state = 2
        self.sigPosicion()
      else:
        self.sigPosicion()

    #Estado 2
    elif self.state == 2:
      if c.isdigit() and int(c) >= 0:
        self.state = 3
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    #Estado 4
    elif self.state == 4:
      if c == '|':
        self.state = 5
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    #Estado 6
    elif self.state == 6:
      if c == '&':
        self.state = 7
        self.sigPosicion()
      else:
        self.tipoDato(-1)


    elif self.state == 10:
      if c == '=':
        self.state = 11
        self.sigPosicion()
      else:
        self.tipoDato(-1)


    elif self.state == 12:
      if c == '=':
        self.state = 13
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    elif self.state == 14:
      if c == '=':
        self.state = 15
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    elif self.state == 16:
      if c == '=':
        self.state = 17
        self.sigPosicion()
      else:
        self.tipoDato(-1)



    #Avanza
    else:
      self.sigPosicion()

  def sigPosicion(self):
    self.pos += 1
    if self.termino():
      self.tipoDato(self.state)
    else:
      if self.newCadena():
        self.tipoDato(self.state)
        self.inicializar()
      else:
        self.asignarEstado(self.string[self.pos])
      


  def tipoDato(self, estado):
    if estado == 1:
        print ('INT')
    elif estado == 3:
        print ('FLOAT')
    elif estado == 5:
        print('OR')
    elif estado == 7:
        print('AND')
    elif estado == 8:
        print('MULTIPL')
    elif estado == 9:
        print('DIVI')
    elif estado == 10:
        print('ASIGNACION')
    elif estado == 11:
        print('COMPARACION')
    elif estado == 12:
        print('MENOR QUE')
    elif estado == 13:
        print('MENOR O IGUAL QUE')
    elif estado == 14:
        print('MAYOR QUE')
    elif estado == 15:
        print('MAYOR O IGUAL QUE')
    elif estado == 17:
        print('DIFERENTE')
    elif estado == 18:
        print('PAREN DER')
    elif estado == 19:
        print('PAREN IZQ')
    elif estado == 20:
        print('LLAVE IZQ')
    elif estado == 21:
        print('LLAVE DER')
    elif estado == 22:
        print('PUNTO Y COMA')
    elif estado == 23:
        print('PLUS')
    elif estado == 24:
        print('MINUS')
    else:
        print ('Invalid')

  def termino(self):
    return self.pos >= self.size

  def newCadena(self):
    if self.string[self.pos] == ' ' and self.pos < self.size:
      return True
    else: 
      return False

  def inicializar(self):
    self.state = 0
    self.valid = True
    self.sigPosicion()



cadena = input('Ingresar cadena: ')
lexico = Lexico(cadena)
lexico.sigPosicion();










