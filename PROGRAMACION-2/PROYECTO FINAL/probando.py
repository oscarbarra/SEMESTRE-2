lista = []

for i in range(10):
    lista.append([])
    for j in range(10):
        lista[i].append(0)

for i in range(10):
    for j in range(10):
        print(lista[i][j], end="   ")
    print("\n")


print(lista[0][0])