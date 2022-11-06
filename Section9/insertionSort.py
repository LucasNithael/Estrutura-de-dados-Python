import numpy as np

def InsertionSort(vetor):
  size = len(vetor)
  for i in range(size):
    marcado = vetor[i]
    j = i - 1
    while j >= 0 and marcado < vetor[j]:
      vetor[j+1] = vetor[j]
      j -= 1
    vetor[j+1] = marcado
  return vetor

print(InsertionSort(np.array([10, 9, 8, 7, 2, 0, 3])))
print(InsertionSort(np.array([10, 5, 4, 3, 2, 1, 0])))