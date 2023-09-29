#haciendo la busqueda binaria desde un enunciado
#completado

import random


def bin_serch(lista, recorrido, serch):
    ciclo = 0

    while True:
        ciclo +=1
        mid = len(lista) // 2
        min_value = 0
        max_value = len(lista)

        print(f"mid = {mid}, min = {min_value}, max = {max_value}")
        print(lista[mid])

        #condiciones de termino
        if recorrido == 1 and lista[min_value] == serch:
            print(f"el numero {serch} esta en la posicion 0")
            break

        if lista[mid] == serch:
            print(f"el numero {serch} esta en la posicion {mid} del ciclo {ciclo}")
            break

        #condiciones de utilidad
        elif lista[mid] > serch:
            max_value = mid
            lista = lista[min_value : max_value]

        elif lista[mid] < serch:
            min_value = mid
            lista = lista[min_value : max_value]

        #exepcion
        else:
            print(f"aparentemente el numero {serch} no forma parte de la lista")

#main
lista = [i for i in range(1, 1000)]
recorrido = len(lista)
serch = random.randint(1, 1000)


bin_serch(lista, recorrido, serch)