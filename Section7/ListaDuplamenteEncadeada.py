class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    self.anterior = None

  def mostra_no(self):
    print(self.valor, end='<->')


class Lista:
  def __init__(self):
    self.primeiro = None
    self.ultimo = None

  def insere_inicio(self, valor):
    novo = No(valor)
    if self.primeiro == None:
      self.primeiro = novo
      self.ultimo =  novo
    else:
      self.primeiro.anterior = novo
      novo.proximo = self.primeiro
      self.primeiro = novo

  def insere_fim(self, valor):
    novo = No(valor)
    if self.primeiro == None:
      self.primeiro = novo
      self.ultimo = novo
    else:
      self.ultimo.proximo = novo
      novo.anterior = self.ultimo
      self.ultimo = novo
   
  def excluir_inicio(self):
    if self.primeiro == None:
      return None
    if self.primeiro.proximo == None:
      temp = self.primeiro.valor
      self.primeiro = None
      return temp
    temp = self.primeiro.valor
    self.primeiro = self.primeiro.proximo
    self.primeiro.anterior = None
    return temp

  def excluir_fim(self):
    if self.primeiro == None:
      return None
    if self.primeiro.proximo == None:
      temp = self.primeiro.valor
      self.primeiro = None
      return temp
    temp = self.ultimo.valor
    self.ultimo = self.ultimo.anterior
    self.ultimo.proximo = None
    return temp     

  def mostrar(self):
    if self.primeiro == None:
      return print("Lista vazia")
    atual = self.primeiro
    while atual!=None:
      atual.mostra_no()
      atual = atual.proximo


l = Lista()
l.insere_inicio(1)


print(l.excluir_inicio())
print(l.excluir_inicio())
print(l.excluir_fim())



l.mostrar()

