class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
  
  def mostra_no(self):
    print(self.valor, end='->')


class Lista:
  def __init__(self):
    self.primeiro = None
    self.ultimo = None

  def insere_inicio(self, valor):
    novo = No(valor)
    if self.primeiro == None:
      self.ultimo = novo
    novo.proximo = self.primeiro
    self.primeiro = novo

  def insere_fim(self, valor):
    novo = No(valor)
    if self.primeiro == None:
      self.primeiro = novo
    else:
      self.ultimo.proximo = novo
    self.ultimo = novo

  def excluir_inicio(self):
    if self.primeiro == None:
      return None
    temp = self.primeiro
    self.primeiro = self.primeiro.proximo
    return temp

  def excluir_fim(self):
    if self.primeiro == None:
      return None
    
    
  def mostrar(self):
    if(self.primeiro == None):
      return print("Lista vazia")
    atual = self.primeiro
    while atual != None:
      atual.mostra_no()
      atual = atual.proximo

l = Lista()
l.insere_inicio(1)
l.insere_inicio(2)
l.insere_inicio(3)
l.insere_fim(10)
l.insere_fim(11)

l.excluir_inicio()
l.excluir_inicio()

l.mostrar()