from math import floor, inf
from random import randint
from copy import deepcopy

def xor(A, B):
  A = deepcopy(lista_A)
  B = deepcopy(lista_B)
  A.append(inf)
  B.append(inf)
  print(len(A), "A: ", A)
  print(len(B), "B: ", B)
  i = j = 0
  C = list()
  print("i j k")
  k = 2
  while k <= len(A) + len(B):
    print(i, j, k)
    if A[i] < B[j]:
      C.append(A[i])
      i += 1
    else:
      if A[i] != B[j]:
        C.append(B[j])
      else:
        i += 1
        k += 1
      j += 1
    print(C)
    k += 1
  return C

