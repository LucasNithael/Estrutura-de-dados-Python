for i in range(5):
  print("Lucas")

def recursao(x):
  print("Nithael")
  x += 1
  if x == 5:
    return
  return recursao(x)

recursao(0)