def ler_temperatura():
  temperatura = float(input("Temperatura: "))
  return converter(temperatura)

def converter(t):
  f = (9 * t + 160)/5
  return f

def mostrar():
  print("Fahrenheit:",ler_temperatura())

mostrar()
