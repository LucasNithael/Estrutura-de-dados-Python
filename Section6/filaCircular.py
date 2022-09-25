import numpy as np

class FilaCircular:
  def __init__(self, capacidade):
    self.__capacidade = capacidade
    self.__inicio = 0
    self.__fim = -1
    self.__numero_elemento = 0
    self.__valores = np.empty(self.__capacidade, dtype=int)

  def __fila_vazia(self):
    return self.__numero_elemento == 0

  def __fila_cheia(self):
    return self.__numero_elemento == self.__capacidade

  def enfileirar(self, valor):
    if self.__fila_cheia():
      return print("Fila cheia")
    if self.__fim == self.__capacidade - 1:
      self.__fim = -1
    self.__fim += 1
    self.__valores[self.__fim] = valor
    self.__numero_elemento += 1

  def desenfileirar(self):
    if self.__fila_vazia():
      return print("Fila vazia")
    temp = self.__valores[self.__inicio]
    self.__inicio += 1
    if self.__inicio == self.__capacidade:
      self.__inicio = 0
    self.__numero_elemento -= 1
    return temp

  def primeiro(self):
    if self.__fila_vazia():
      return -1
    return self.__valores[self.__inicio]

fila = FilaCircular(5)
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
print(fila.desenfileirar())
print(fila.desenfileirar())
print(fila.desenfileirar())
print(fila.desenfileirar())
print(fila.desenfileirar())
fila.enfileirar(10)
#print(fila.desenfileirar())
print(fila.primeiro())
print(fila.primeiro())



