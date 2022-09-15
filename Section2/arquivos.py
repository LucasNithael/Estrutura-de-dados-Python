alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('Section2/alunos.txt', 'w') as texto:
  for aluno, nota in alunos.items():
    texto.write(f"{aluno}, {nota}\n")

with open('Section2/alunos.txt', 'r') as texto:
  for i in texto:
    print(i)

