dic = {}
for _ in range(3):
  nome = input("Nome: ")
  nota = int(input("Nota: "))
  dic[nome] = nota

media = 0
for i in dic.values():
  media += i

print("Média:",media/3)