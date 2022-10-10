

class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    
  def mostra_no(self):
    print(self.valor)

class ListaEncadeada:
  def __init__(self):
    self.primeiro = None

  def insere_inicio(self, valor):
    novo = No(valor)
    novo.proximo = self.primeiro
    self.primeiro = novo

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
l.mostrar()