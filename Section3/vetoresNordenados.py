import numpy as np

class VetorNaoOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
      if self.ultima_posicao == -1:
            print("Vetor vazio")
      else:
        for i in range(self.ultima_posicao + 1):
          print(i, '-', self.valores[i])
    # O(2)
    def insere(self, valor):
      if self.capacidade - 1 == self.ultima_posicao:
        print("Vetor atingiu a capacidade máxima")
      else:
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor
    
    # O(n)
    def pesquisar(self, valor):
      for i in range(self.ultima_posicao+1):
        if valor==self.valores[i]:
          return i
      return -1

    # O(n)
    def excluir(self, valor):
      self.index = self.pesquisar(valor)
      if self.index == -1: 
        return print("Valor não existe")
      for i in range(self.index, self.ultima_posicao):
        self.valores[i] = self.valores[i+1]
      self.ultima_posicao -= 1
        

v = VetorNaoOrdenado(5)
#v.imprime()

v.insere(5)
v.insere(6)
v.insere(4)
v.insere(33)
v.insere(10)
v.excluir(33)
v.excluir(33)
v.imprime()
print(v.pesquisar(5))
