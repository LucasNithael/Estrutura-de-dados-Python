
class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    
  def mostra_no(self):
    print(self.valor, end='->')

class ListaEncadeada:
  def __init__(self):
    self.primeiro = None

  def insere_inicio(self, valor):
    novo = No(valor)
    novo.proximo = self.primeiro
    self.primeiro = novo

  def exclue_inicio(self):
    if self.primeiro==None:
      return None
    temp = self.primeiro.valor
    self.primeiro = self.primeiro.proximo
    return temp

  def pesquisar(self, valor):
    if self.primeiro == None:
      return None
    atual = self.primeiro
    while atual.valor != valor:
      if atual.proximo == None:
        return None
      atual = atual.proximo
    return atual.valor

  def excluir_index(self, index):
    if self.primeiro == None:
      return None
    if index==0:
      self.primeiro = self.primeiro.proximo
      return
    atual = self.primeiro
    for i in range(index-1):
      if atual.proximo == None:
        return None
      atual = atual.proximo
    atual.proximo = atual.proximo.proximo
    return atual

  def excluir_elemento(self, valor):
    if self.primeiro == None:
      return None
    atual = self.primeiro
    anterior = self.primeiro
    while atual.valor != valor:
      if atual.proximo == None:
        return None
      anterior = atual
      atual = atual.proximo
    if atual == self.primeiro:
      self.primeiro = self.primeiro.proximo
    else:
      anterior.proximo = atual.proximo
    

  def mostrar(self):
    if(self.primeiro == None):
      return print("Lista vazia")
    atual = self.primeiro
    while atual != None:
      atual.mostra_no()
      atual = atual.proximo


l = ListaEncadeada()
l.insere_inicio(2)
l.insere_inicio(7)
l.insere_inicio(3)
l.insere_inicio(4)
l.insere_inicio(5)
print(l.pesquisar(4))
l.excluir_index(4)
l.excluir_elemento(5)

#5->4->3->7->2-

#l.exclue_inicio()
#l.exclue_inicio()
l.mostrar()