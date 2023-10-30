#El problema es el siguiente: Dado un conjunto de monedas con diferentes denominaciones y una cantidad total, 
#encuentre el número mínimo de monedas que suman esa cantidad. Si no es posible hacer la cantidad con las monedas dadas,
#devuelve -1.

#Ejemplo: Si las monedas son [1, 2, 5] y la cantidad es 11, la respuesta es 3 porque 11 = 5 + 5 + 1.

#Usamos programación dinámica para evitar la reevaluación de los resultados. 
#La idea es construir una tabla dp donde dp[i] representará el número mínimo de monedas requeridas para la cantidad i.

import time

def min_cantidad_monedas(monedas, indice, total):
    recomendar = [] #lista min cantidad de monedas que suman el total
    while sum(recomendar) < total:
        if sum(recomendar) +monedas[indice] == total:
            recomendar.append(monedas[indice])
            
        elif sum(recomendar) +monedas[indice] < total:
            recomendar.append(monedas[indice])

        elif sum(recomendar) +monedas[indice] > total:
            indice -=1
    return recomendar

star_time = time.time()
monedas_disponibles = [1, 2, 5, 10, 20]
indice = len(monedas_disponibles) -1
total_requerido = int(input("ingresar el valor nesecitado: "))
min_monedas = min_cantidad_monedas(monedas_disponibles, indice, total_requerido)

end_time = time.time()
print(f"la minima cantidad de monedas que suman {total_requerido} son: {min_monedas}")
print(f"el tiempo de ejecucion fue de {end_time -star_time}")