import time

#fibonashi dinamico

def fib_dinamico(lista, indice, num):
    for i in range(indice, num):
        fibonacci = lista[i-1] + lista[i-2]
        lista.append(fibonacci)
        indice +=1
    
    return lista[indice-1]


indice = 2
num = int(input("ingresar un numero NATURAL: "))
lista = [0, 1]
star_tiempo = time.time()

print(fib_dinamico(lista, indice, num+1))

end_tiempo = time.time()

print(f"el tiempo de ejecucion fue de {end_tiempo - star_tiempo}")