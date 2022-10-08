from copy import deepcopy
inconsistente = 0
achou = 1
expandir = 2
def avaliacao(n, x):
    j = n - x.count(-1)
    for i in range(j-1):
        if x[i] == x[j-1] or abs(x[i] - x[j-1]) == abs(i - (j-1)):
            return inconsistente
    if j == n:
        return achou
    else:
        return expandir

def n_rainhas(n):
  ''' estrutura inicial - f '''
  f = [[-1 for x in range(n)] for y in range(n)]
  for x in range(n):
    f[x][0] = x

  tem_solucao = False
  while len(f) > 0:
    x = f.pop()
    resultado = avaliacao(n, x)
    if resultado == achou:
        print("Resultado:", x)
        tem_solucao = True
        ''' comentar a próxima linha para dar todos os resultados ou
            descomentar a próxima linha para dar apenas o primeiro resultado.
        '''
        #f = []
    elif resultado == expandir:
        #print(x)
        j = n - x.count(-1)
        for i in range(n):
            x1 = deepcopy(x)
            x1[j] = i
            f.append(x1)
    elif resultado == inconsistente:
      pass
        #print("Inconsistente:", x)
  if not tem_solucao:
    print("Não existe solução")

if __name__ == "__main__":
  N = 4
  n_rainhas(N)

