lista = []
try:
  for _ in range(2):
    n = float(input("Valor: "))
    lista.append(n)

  print(lista[0]/lista[1])
except ValueError:
  print("Valor invalido")
except ZeroDivisionError:
  print("Divisão por zero")
except IndexError:
  print("Índice invalido")
except KeyboardInterrupt:
  print("Úsuario parou programa")