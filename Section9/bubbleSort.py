import numpy as np

def BubbleSort(vetor):
  size = len(vetor)
  for i in range(size):
    for j in range(size-i-1):
      if vetor[j] > vetor[j+1]:
        temp = vetor[j]
        vetor[j] = vetor[j+1]
        vetor[j+1] = temp
  return vetor


print(BubbleSort(np.array([10, 9, 8, 7, 2, 0, 3])))