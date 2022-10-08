from random import randint
from math import floor, inf
from copy import deepcopy

def merge_sort(A, inicio, fim):
  if inicio >= fim:
    return
  else:
    meio = floor((inicio+fim) / 2)
    merge_sort(A, inicio, meio)
    merge_sort(A, meio+1, fim)
    merge(A, inicio, meio, fim)

def merge(A, inicio, meio, fim):
  #n1 = meio - inicio + 1
  #n2 = fim - meio
  B = deepcopy(A[inicio : meio+1])
  C = deepcopy(A[meio+1 : fim+1])
  B.append(inf)
  C.append(inf)
  print(len(B), "B: ", B)
  print(len(C), "C: ", C)
  i = j = 0
  for k in range(inicio, fim+1):
    if B[i] <= C[j]:
      A[k] = B[i]
      i += 1
    else:
      A[k] = C[j]
      j += 1
if __name__ == '__main__':
  N = 20
  A = [randint(0,100) for x in range(N)]
  print(A)
  merge_sort(A,0, N-1)
  print(A)
