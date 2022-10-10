

vvsdvimport numpy as np

class Pilha:
  def __init__(self, capacidade):
    self.__capacidade = capacidade
    self.__topo = -1
    self.__valores = np.empty(self.__capacidade, dtype=int)

  def __pilha_cheia(self):
    if self.__topo == self.__capacidade - 1:
      return True
    return False

  def __pilha_vazia(self):
    if self.__topo == -1:
      return True
    return False

  def empilhar(self, valor):
    if self.__pilha_cheia():
      return print("Pliha cheia")
    self.__topo += 1
    self.__valores[self.__topo] = valor

  def desempilhar(self):
    if self.__pilha_vazia():
      return print("Pilha vazia")
    self.__topo -= 1

  def ver_topo(self):
    if self.__topo != -1:
      return self.__valores[self.__topo]
    else:
      return -1

pilha = Pilha(5)
pilha.empilhar(8)
pilha.empilhar(5)
pilha.empilhar(7)
pilha.empilhar(20)
pilha.empilhar(12)
print(pilha.ver_topo())
pilha.desempilhar()
print(pilha.ver_topo())
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
print(pilha.ver_topo())



