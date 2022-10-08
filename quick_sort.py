from random import randint
from copy import deepcopy

def quick_sort(A, inicio, fim, contador):
  if inicio >= fim:
    return
  else:
    print("A[", inicio, ":" , fim, "]:", A[inicio : fim+1])
    meio = partition(A, inicio, fim, contador)
    print("meio=", meio)
    quick_sort(A, inicio, meio-1, contador)
    quick_sort(A, meio+1, fim, contador)

def partition(A, inicio, fim, contador):
  meio = inicio
  for u in range(inicio, fim):
    #print("u:", u, "fim:", fim)
    contador[0] += 1
    if A[u] <= A[fim]:
      contador[1] += 1
      swap(A, meio, u)
      meio += 1
      print("meio:", meio, "A[", inicio, ":" , fim, "]:", A[inicio : fim+1])
  contador[1] += 1
  swap(A, meio, fim)
  print(A)
  return meio

def swap(A, i, j):
  aux = A[i]
  A[i] = A[j]
  A[j] = aux

if __name__ == "__main__":
  N = 6
  contador = [0, 0]
  A = [randint(0,100) for x in range(N)]
  print("Vetor Inicial:", A)
  quick_sort(A,0, N-1, contador)
  print("Vetor Final:", A)
  print("Comparacoes:", contador[0], "Trocas:", contador[1])
