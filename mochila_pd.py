

def mochila_inteira_iterativa(S, n, W):
  M = [[0 for _ in range(0,W+1)] for _ in range(0, n+1)]
  for j in range(1, n+1):
    for X in range(1, W+1):
      if S[j-1][0] > X:
        M[j][X] = M[j-1][X]
      else:
        usar = S[j-1][1] + M[j-1][X-S[j-1][0]]
        nao_usar = M[j-1][X]
        M[j][X] = max(usar, nao_usar)
  return M


def mochila_inteira_solucao(S, M, W, n):
    Solucao = []
    x = W
    j = n
    while j >= 1:
        print("x: ",x,"  j: ", j)
        if M[j][x] == M[j-1][x - S[j-1][0]] + S[j-1][1]:
            Solucao.append(S[j-1])
            x -= S[j-1][0]
        j -= 1
    return Solucao


if __name__ == "__main__":
    S = [(1,6), (3, 15), (3,12), (4,16), (5,20), (5,15), (6,6)]
    W = 6

    M = mochila_inteira_iterativa(S, 7, 6)
    for linha in M:
        print(linha)

    print(mochila_inteira_solucao(S, M, W, 7))


