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
      elif c == 'i':
        self.state = 25
        self.sigPosicion()
      elif c == 'w':
        self.state = 28
        self.sigPosicion()
      elif c == 'r':
        self.state = 33
        self.sigPosicion()
      elif c == 'e':
        self.state = 39
        self.sigPosicion()
      elif c == 'f':
        self.state = 45
        self.sigPosicion()
      elif c == '"':
        self.state = 50
        self.sigPosicion()
     
      elif c.isalpha():
        self.state = 27
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

    #Estado 10
    elif self.state == 10:
      if c == '=':
        self.state = 11
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    #Estado 12
    elif self.state == 12:
      if c == '=':
        self.state = 13
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    #Estado 14
    elif self.state == 14:
      if c == '=':
        self.state = 15
        self.sigPosicion()
      else:
        self.tipoDato(-1)
        
    #Estado 16
    elif self.state == 16:
      if c == '=':
        self.state = 17
        self.sigPosicion()
      else:
        self.tipoDato(-1)


    #Estado 25
    elif self.state == 25:
      if c == 'f':
        self.state = 26
        self.sigPosicion()
      elif c == 'n':
        self.state = 43
        self.sigPosicion()
      else:
        self.state = 27
        self.sigPosicion()


    #Estado 26
    elif self.state == 26:
      if c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else:
        self.tipoDato(-1)


    #Estado 27
    elif self.state == 27:
      if c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    #Estado 28
    elif self.state == 28:
      if c == 'h':
        self.state = 29
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

     #Estado 29
    elif self.state == 29:
      if c == 'i':
        self.state = 30
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

     #Estado 30
    elif self.state == 30:
      if c == 'l':
        self.state = 31
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    #Estado 31
    elif self.state == 31:
      if c == 'e':
        self.state = 32
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    #Estado 32
    elif self.state == 32:
      if c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    #Estado 33
    elif self.state == 33:
      if c == 'e':
        self.state = 34
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    #Estado 34
    elif self.state == 34:
      if c == 't':
        self.state = 35
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)


    #Estado 35
    elif self.state == 35:
      if (c == 'u'):
        self.state = 36
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    #Estado 36
    elif self.state == 36:
      if c == 'r':
        self.state = 37
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    #Estado 37
    elif self.state == 37:
      if c == 'n':
        self.state = 38
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    #Estado 38
    elif self.state == 38:
      if c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    #Estado 39
    elif self.state == 39:
      if c == 'l':
        self.state = 40
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    elif self.state == 40:
      if c == 's':
        self.state = 41
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)


    elif self.state == 41:
      if c == 'e':
        self.state = 42
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    
    elif self.state == 42:
      if c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    elif self.state == 43:
      if c == 't':
        self.state = 44
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    elif self.state == 44:
      if c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    elif self.state == 45:
      if c == 'l':
        self.state = 46
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    elif self.state == 46:
      if c == 'o':
        self.state = 47
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    elif self.state == 47:
      if c == 'a':
        self.state = 48
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    elif self.state == 48:
      if c == 't':
        self.state = 49
        self.sigPosicion()
      elif c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else: 
        self.tipoDato(-1)

    elif self.state == 49:
      if c.isdigit() or c.isalpha():
        self.state = 27
        self.sigPosicion()
      else:
        self.tipoDato(-1)

    elif self.state == 50:
      if c == '"':
        self.state = 51
        self.sigPosicion()
      else:
        self.state = 50
        self.sigPosicion()
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
        print ('INTNUMB')
    elif estado == 3:
        print ('FLOATNUMB')
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
    elif estado == 26:
        print('IF')
    elif estado == 25 or estado == 27 or estado == 28 or estado == 29 or estado == 30 or estado == 31 or estado == 33 or estado == 34 or estado == 35 or estado == 36 or estado == 37 or estado == 39 or estado == 40 or estado == 41 or estado == 43 or estado == 45 or estado == 46 or estado == 47 or estado == 48:
        print('IDENTIFICADOR')
    elif estado == 32:
        print('WHILE')
    elif estado == 38:
        print('RETURN')
    elif estado == 42:
        print('ELSE')
    elif estado == 44:
        print('INT')
    elif estado == 49:
        print('FLOAT')
    elif estado == 51:
        print('CADENA')

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










