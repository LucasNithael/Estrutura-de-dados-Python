import numpy as np

class FilaPrioridade:
  def __init__(self, capacidade):
    self.__capacidade = capacidade
    self.numero_elemento = 0
    self.valores = np.empty(self.__capacidade, dtype=int)

  def __fila_cheia(self):
    return self.__capacidade == self.numero_elemento

  def fila_vazia(self):
    return self.numero_elemento == 0

  def enfileirar(self, valor):
    if self.__fila_cheia():
      return print("Fila cheia")
    if self.numero_elemento == 0:
      self.valores[self.numero_elemento] = valor
      self.numero_elemento += 1
    else:
      x = self.numero_elemento - 1
      while x >= 0:
        if valor > self.valores[x]:
          self.valores[x+1] = self.valores[x]
        else:
          break
        x -= 1
      self.valores[x + 1] = valor
      self.numero_elemento += 1

  def desenfileirar(self):
    if self.fila_vazia():
      return print("Fila vazia")
    element = self.valores[self.numero_elemento-1] 
    self.numero_elemento -= 1
    return element

f = FilaPrioridade(5)
f.enfileirar(10)
f.enfileirar(30)
f.enfileirar(20)
print(f.desenfileirar())
f.enfileirar(9)
print(f.desenfileirar())
