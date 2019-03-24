class Pila():
  def __init__(self):
    self.pila = list()

  def push(self, element):
    self.pila.append(element)

  def pop(self):
    self.pila.pop()

  def pop(self,size):
    for i in range(0,size):
      self.pila.pop()

  def get(self):
    return self.pila
  def top(self):
    return self.pila[-1]