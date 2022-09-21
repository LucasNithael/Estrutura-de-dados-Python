
class Aluno:
  def __init__(self, nome, n1, n2):
    self.nome = nome
    self.nota1 = n1
    self.nota2 = n2
    self.media = 0.0
  def Media(self):
    self.media = (self.nota1+self.nota2)/2
    return self.media
  def Dados(self):
      return f"{self.nome} - Média {self.media}"
  def Resultado(self):
    if self.media<60:
      return False
    else:
      return True
      
a1 = Aluno("Lucas", 10, 5)
print(a1.Media())
print(a1.Dados())
print(a1.Resultado())
