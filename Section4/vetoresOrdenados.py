import numpy as np

class VetorOrdenado:
  
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
    
    # O(n)
    def insere(self, valor):
      if self.ultima_posicao == self.capacidade:
        return print("Vetor cheio")
      posicao = 0
      for i in range(self.ultima_posicao+1):
        if self.valores[i] > valor:
          posicao = i
          break
        if i == self.ultima_posicao:
          posicao = i+1
      x = self.ultima_posicao
      while x >= posicao:
        self.valores[x + 1] = self.valores[x]
        x -= 1
      self.valores[posicao] = valor
      self.ultima_posicao += 1

    # O(n)
    def pesquisa_linear(self, valor):
      for i in range(self.ultima_posicao+1):
        if self.valores[i] > valor:
          return -1
        if self.valores[i] == valor:
          return i
        if i == self.ultima_posicao:
          return -1

    def excluir(self, valor):
      self.posicao = self.pesquisar(valor)
      if self.posicao == -1:
        return -1
      for i in range(self.posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i+1]
      self.ultima_posicao -= 1

    # o(log n)
    def pesquisa_binaria(self, valor):
      limite_inferior = 0
      limite_superior = self.ultima_posicao
      
      while True:
        posicao_atual = int((limite_inferior + limite_superior)/2)
        # Achou na primeira tentativa
        if self.valores[posicao_atual] == valor:
          return posicao_atual
        # Se não achou
        elif limite_inferior > limite_superior:
          return -1
        # Divide os limites
        else:
          # Limite inferior
          if self.valores[posicao_atual] < valor:
            limite_inferior = posicao_atual + 1
          # Limite superior
          else:
            limite_superior = posicao_atual - 1
            

      

v = VetorOrdenado(10)
v.insere(10)
v.insere(12)
v.insere(4)
v.insere(9)
v.insere(1)
v.insere(7)
v.insere(2)
#print(v.pesquisa_linear(5))
v.excluir(12)
print(v.pesquisa_binaria(999))
v.imprime()