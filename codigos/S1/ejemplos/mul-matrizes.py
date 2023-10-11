import time

def multiply_matrices(X, Y):
    #array temporal
    result = [[0 for _ in range(len(X))] for _ in range(len(Y[0]))]
    #filas del array x
    for i in range(len(X)): #100
        #columnas del array y
        for j in range(len(Y[0])): #100
            #filas del array y
            for k in range(len(Y)): #100
                #contenedor de la suma//columnas//filas
                result[i][j] += X[i][k] * Y[k][j]
    return result

#condicion
#c array x = f array y && c array y = f array x

X = [[1 for _ in range(10)] for _ in range(20)]
Y = [[1 for _ in range(20)] for _ in range(10)]

start_time = time.time()
#multiply_matrices(X, Y)
end_time = time.time()

print(f"El tiempo de ejecución fue de {end_time - start_time} segundos")
print(multiply_matrices(X, Y))