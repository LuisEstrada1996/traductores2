import os
os.system('clear')

class Lexico():
  def __init__(self, string):
    self.state = 0
    self.string = string
    self.pos = -1
    self.valid = True
    self.size = len(string)
    self.boolToken = False
    self.token = 0

  def asignarEstado(self, c):
    #Estado 0
    if self.state == 0:
      if c.isdigit() and int(c) >= 0:
        self.state = 1
        
      elif c == '|':
        self.state = 4
        
      elif c == '&':
        self.state = 6
        
      elif c == '*':
        self.state = 8
        
      elif c == '/':
        self.state = 9
        
      elif c == '=':
        self.state = 10
        
      elif c == '<':
        self.state = 12
        
      elif c == '>':
        self.state = 14
        
      elif c == '!':
        self.state = 16
        
      elif c == '(':
        self.state = 18
        
      elif c == ')':
        self.state = 19
        
      elif c == '{':
        self.state = 20
        
      elif c == '}':
        self.state = 21
        
      elif c == ';':
        self.state = 22
        
      elif c == '+':
        self.state = 23
        
      elif c == '-':
        self.state = 24
        
      elif c == 'i':
        self.state = 25
        
      elif c == 'w':
        self.state = 28
        
      elif c == 'r':
        self.state = 33
        
      elif c == 'e':
        self.state = 39
        
      elif c == 'f':
        self.state = 45
        
      elif c == '"':
        self.state = 50
        
     
      elif c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    #Estado 1
    elif self.state == 1:
      if c == '.':
        self.state = 2

    #Estado 2
    elif self.state == 2:
      if c.isdigit() and int(c) >= 0:
        self.state = 3
        
      else: 
        self.tipoDato(-1)

    #Estado 4
    elif self.state == 4:
      if c == '|':
        self.state = 5
        
      else:
        self.tipoDato(-1)

    #Estado 6
    elif self.state == 6:
      if c == '&':
        self.state = 7
        
      else:
        self.tipoDato(-1)

    #Estado 10
    elif self.state == 10:
      if c == '=':
        self.state = 11
        
      else:
        self.tipoDato(-1)

    #Estado 12
    elif self.state == 12:
      if c == '=':
        self.state = 13
        
      else:
        self.tipoDato(-1)

    #Estado 14
    elif self.state == 14:
      if c == '=':
        self.state = 15
        
      else:
        self.tipoDato(-1)
        
    #Estado 16
    elif self.state == 16:
      if c == '=':
        self.state = 17
        
      else:
        self.tipoDato(-1)


    #Estado 25
    elif self.state == 25:
      if c == 'f':
        self.state = 26
        
      elif c == 'n':
        self.state = 43
        
      else:
        self.state = 27
        


    #Estado 26
    elif self.state == 26:
      if c.isdigit() or c.isalpha():
        self.state = 27
        
      else:
        self.tipoDato(-1)


    #Estado 27
    elif self.state == 27:
      if c.isdigit() or c.isalpha():
        self.state = 27
        
      else:
        self.tipoDato(-1)

    #Estado 28
    elif self.state == 28:
      if c == 'h':
        self.state = 29
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

     #Estado 29
    elif self.state == 29:
      if c == 'i':
        self.state = 30
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

     #Estado 30
    elif self.state == 30:
      if c == 'l':
        self.state = 31
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    #Estado 31
    elif self.state == 31:
      if c == 'e':
        self.state = 32
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    #Estado 32
    elif self.state == 32:
      if c.isdigit() or c.isalpha():
        self.state = 27
        
      else:
        self.tipoDato(-1)

    #Estado 33
    elif self.state == 33:
      if c == 'e':
        self.state = 34
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    #Estado 34
    elif self.state == 34:
      if c == 't':
        self.state = 35
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)


    #Estado 35
    elif self.state == 35:
      if (c == 'u'):
        self.state = 36
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    #Estado 36
    elif self.state == 36:
      if c == 'r':
        self.state = 37
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else:
        self.tipoDato(-1)

    #Estado 37
    elif self.state == 37:
      if c == 'n':
        self.state = 38
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    #Estado 38
    elif self.state == 38:
      if c.isdigit() or c.isalpha():
        self.state = 27
        
      else:
        self.tipoDato(-1)

    #Estado 39
    elif self.state == 39:
      if c == 'l':
        self.state = 40
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    elif self.state == 40:
      if c == 's':
        self.state = 41
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)


    elif self.state == 41:
      if c == 'e':
        self.state = 42
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    
    elif self.state == 42:
      if c.isdigit() or c.isalpha():
        self.state = 27
        
      else:
        self.tipoDato(-1)

    elif self.state == 43:
      if c == 't':
        self.state = 44
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    elif self.state == 44:
      if c.isdigit() or c.isalpha():
        self.state = 27
        
      else:
        self.tipoDato(-1)

    elif self.state == 45:
      if c == 'l':
        self.state = 46
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    elif self.state == 46:
      if c == 'o':
        self.state = 47
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    elif self.state == 47:
      if c == 'a':
        self.state = 48
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    elif self.state == 48:
      if c == 't':
        self.state = 49
        
      elif c.isdigit() or c.isalpha():
        self.state = 27
        
      else: 
        self.tipoDato(-1)

    elif self.state == 49:
      if c.isdigit() or c.isalpha():
        self.state = 27
        
      else:
        self.tipoDato(-1)

    elif self.state == 50:
      if c == '"':
        self.state = 51
        
      else:
        self.state = 50
              




  def sigPosicion(self):
    self.pos += 1
  
    if self.newCadena():
      self.tipoDato(self.state)
      self.inicializar()
    else:
      self.asignarEstado(self.string[self.pos])
    

    
      


  def tipoDato(self, estado):
    self.boolToken = True;
    if estado == 1:
        self.token = 'INT'
    elif estado == 3:
        self.token = 'FLOAT'
    elif estado == 5:
        self.token = 'OR'
    elif estado == 7:
        self.token = 'AND'
    elif estado == 8:
        self.token = 'MULTIPL'
    elif estado == 9:
        self.token = 'DIVI'
    elif estado == 10:
        self.token = 'ASIGNACION'
    elif estado == 11:
        self.token = 'COMPARACION'
    elif estado == 12:
        self.token = 'MENOR QUE'
    elif estado == 13:
        self.token = 'MENOR O IGUAL QUE'
    elif estado == 14:
        self.token = 'MAYOR QUE'
    elif estado == 15:
        self.token = 'MAYOR O IGUAL QUE'
    elif estado == 17:
        self.token = 'DIFERENTE'
    elif estado == 18:
        self.token = 'PAREN DER'
    elif estado == 19:
        self.token = 'PAREN IZQ'
    elif estado == 20:
        self.token = 'LLAVE IZQ'
    elif estado == 21:
        self.token = 'LLAVE DER'
    elif estado == 22:
        self.token = 'PUNTO Y COMA'
    elif estado == 23:
        self.token = 'PLUS'
    elif estado == 24:
        self.token = 'MINUS'
    elif estado == 26:
        self.token = 'IF'
    elif estado == 25 or estado == 27 or estado == 28 or estado == 29 or estado == 30 or estado == 31 or estado == 33 or estado == 34 or estado == 35 or estado == 36 or estado == 37 or estado == 39 or estado == 40 or estado == 41 or estado == 43 or estado == 45 or estado == 46 or estado == 47 or estado == 48:
        self.token = 'ID'
    elif estado == 32:
        self.token = 'WHILE'
    elif estado == 38:
        self.token = 'RETURN'
    elif estado == 42:
        self.token = 'ELSE'
    elif estado == 44:
        self.token = 'INT'
    elif estado == 49:
        self.token = 'FLOAT'
    elif estado == 51:
        self.token = 'CADENA'
    else:
        self.token = 'INVALID'

  def termino(self):
    return self.pos >= self.size-1

  def newCadena(self):
    if self.string[self.pos] == ' ' and self.pos < self.size:
      return True
    else: 
      return False

  def inicializar(self):
    self.state = 0
    self.valid = True
    self.sigPosicion()


















