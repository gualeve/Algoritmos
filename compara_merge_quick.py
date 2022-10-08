from random import randint
from math import floor, inf
from copy import deepcopy

def quick_sort(A, inicio, fim, contador):
  if inicio >= fim:
    return
  else:
    #print("A[", inicio, ":" , fim, "]:", A[inicio : fim+1])
    meio = partition(A, inicio, fim, contador)
    #print("meio=", meio)
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
      #print("meio:", meio, "A[", inicio, ":" , fim, "]:", A[inicio : fim+1])
  contador[1] += 1
  swap(A, meio, fim)
  #print(A)
  return meio

def swap(A, i, j):
  aux = A[i]
  A[i] = A[j]
  A[j] = aux

def merge_sort(A, inicio, fim, contador):
  if inicio >= fim:
    return
  else:
    meio = floor((inicio+fim) / 2)
    merge_sort(A, inicio, meio, contador)
    merge_sort(A, meio+1, fim, contador)
    merge(A, inicio, meio, fim, contador)

def merge(A, inicio, meio, fim, contador):
  B = deepcopy(A[inicio : meio+1])
  C = deepcopy(A[meio+1 : fim+1])
  B.append(inf)
  C.append(inf)
  #print(len(B), "B: ", B)
  #print(len(C), "C: ", C)
  i = j = 0
  for k in range(inicio, fim+1):
    contador[0] += 1
    if B[i] <= C[j]:
      A[k] = B[i]
      i += 1
    else:
      A[k] = C[j]
      j += 1

def gerar_array(m, n, q):
  '''
  gerar_array(
    m - variedade dos valores gerados
    n - Tamanho do array gerado
    q - agrupamento | 1/N <= q <= 1.0
        q próximo a 1/N gera um vetor mais ordenado
        q próximo a 1.0 gera um vetor menos ordenado
        q igual a 1/N gera um vetor completamente ordenado
  )
  '''
  if (q * n) < 1 or q > 1:
    return []
  grupos = int((1 / q))
  tam_grupos = int(n / grupos)
  faixa = int(m * q)
  A = list()
  fim = -1
  print("grupos:", grupos, "tam_grupos:", tam_grupos)
  for i in range(grupos):
    inicio = fim + 1
    fim = inicio + faixa - 1
    print("inicio:", inicio, "fim:", fim)
    for j in range(tam_grupos):
      A.append(randint(inicio, fim))
  if n % grupos != 0:
    for j in range(tam_grupos * grupos, n):
      A.append(randint(fim, m))
  return A

if __name__ == "__main__":
  N = 20
  A = gerar_array(100, N, 0.2)
  if len(A) == 0:
    print("Erro")
  else:
    B = deepcopy(A)
    contador = [0, 0]
    print("MERGE SORT")
    print(A)
    merge_sort(A,0, N-1, contador)
    print(A)
    print("Comparacoes:", contador[0], "Trocas:", contador[1])

    print("\nQUICK SORT")
    contador = [0, 0]
    print("Vetor Inicial:", B)
    quick_sort(B, 0, N-1, contador)
    print("Vetor Final:", B)
    print("Comparacoes:", contador[0], "Trocas:", contador[1])
