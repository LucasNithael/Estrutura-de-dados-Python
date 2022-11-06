import numpy as np

def SelectionSort(vetor):
  size = len(vetor)
  for i in range(size):
    index_min = i
    for j in range(i+1, size):
      if vetor[index_min] > vetor[j]:
        index_min = j
    temp = vetor[i]
    vetor[i] = vetor[index_min]
    vetor[index_min] = temp
  return vetor

print(SelectionSort(np.array([10, 9, 8, 7, 2, 0, 3])))