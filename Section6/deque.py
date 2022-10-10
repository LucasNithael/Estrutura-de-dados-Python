import numpy as np

class Deque:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.inicio = -1
    self.final = 0
    self.valores = np.empty(self.capacidade, dtype=int)

  def __deque_cheio(self):
    return (self.inicio == 0 and self.final == self.capacidade -1) or (self.inicio == self.final + 1)
    
  def __deque_vazio(self):
    return self.inicio == -1

  def insere_inicio(self, valor):
    if self.__deque_cheio():
      return print("Deque cheio")
    if self.inicio == -1:
      self.inicio = 0
      #self.final = 0
    elif self.inicio == 0:
      self.inicio = self.capacidade - 1
    else:
      self.inicio -= 1

    self.valores[self.inicio] = valor

  def insere_final(self, valor):
    if self.__deque_cheio():
      return print("Deque cheio")
    if self.inicio == -1:
      self.inicio = 0
      #self.final = 0
    elif self.final == self.capacidade - 1:
      self.final = 0
    else:
      self.final += 1

    self.valores[self.final] = valor

  def excluir_inicio(self):
    if self.__deque_vazio():
      return print("Deque vazio")
    if self.inicio == self.final:
      self.final = 0
      self.inicio = -1
    elif self.inicio == self.capacidade - 1:
      self.inicio = 0
    else:
      self.inicio += 1

  def excluir_final(self):
    if self.__deque_vazio():
      return print("Deque vazio")
    if self.final == self.inicio:
      self.final = 0
      self.inicio = -1
    elif self.final == 0:
      self.final = self.capacidade - 1
    else:
      self.final -= 1


d = Deque(5)
d.insere_final(1)
d.insere_final(2)
d.insere_inicio(3)
d.insere_inicio(4)
d.insere_final(5)
d.excluir_final()
print("Indice Final", d.final)
print("Indice Inicio", d.inicio)
print("Valor inicio", d.valores[d.inicio])
print("Valor final", d.valores[d.final])
print(d.valores)
    