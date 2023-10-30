#Supongamos que estás en un país con un sistema monetario peculiar. Las denominaciones de las monedas no son las habituales
#y te enfrentas a la tarea de hacer cambio para una cantidad específica.

#El problema es el siguiente: Dado un conjunto de monedas con diferentes denominaciones y una cantidad total, 
#encuentre el número mínimo de monedas que suman esa cantidad. Si no es posible hacer la cantidad con las monedas dadas,
#devuelve -1.

#Ejemplo: Si las monedas son [1, 2, 5] y la cantidad es 11, la respuesta es 3 porque 11 = 5 + 5 + 1.

import time

def buscar_combinacion_monedas(monedas, indice, total, usar):
    if sum(usar) +monedas[indice] == total:
        usar.append(monedas[indice])

    elif sum(usar) +monedas[indice] < total:
        usar.append(monedas[indice])
        buscar_combinacion_monedas(monedas, indice, total, usar)

    elif sum(usar) +monedas[indice] > total:
        buscar_combinacion_monedas(monedas, indice -1, total, usar)

star_time = time.time()
monedas_disponibles = [1, 2, 5, 10, 20] #tiene que estar ordenado de menor a mayor
indice_mon_disp = len(monedas_disponibles) -1
total_requerido = int(input("ingresar la cantidad deseada de dinero: "))
monedas_usar = [] #almacenara las monedas minimas para alcanzar el total

buscar_combinacion_monedas(monedas_disponibles, indice_mon_disp, total_requerido, monedas_usar)

end_time = time.time()
print(monedas_usar)
print(f"tiempo de ejecucion {end_time -star_time}")