from random import randint
limite_garrafa = 10
pocos = [(x, randint(1,limite_garrafa)) for x in range(10, -1, -1)]
garrafa = limite_garrafa
paradas = []
print("Mapa de Poços:")
print(pocos)
while len(pocos) > 0:
  proximo = pocos.pop()
  garrafa -= proximo[1]
  if garrafa < 0:
    pocos.append(proximo)
    paradas.append(proximo) 
    garrafa = limite_garrafa
print("Pontos de Abastecimentos:")
print(paradas)

