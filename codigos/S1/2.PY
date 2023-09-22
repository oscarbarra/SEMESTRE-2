import random as ra

#TRATAR DED ARREGLAR ESTO   
#buscar un elemento en una lista con bin-sech

def busqueda_binaria_max(lista, serch, numero):
    while lista[serch] != numero:
        busqueda_binaria_max(lista, serch+1, numero)
    return serch


def busqueda_binaria_min(lista, serch, numero):
    while lista[serch] != numero:
        busqueda_binaria_min(lista, serch-1, numero)
    return serch


def principal():
    #creo la lista
    lista = [ra.randint(1,100) for i in range(10)]

    #determino el tamaño completo de la lista 
    tamaño = len(lista)

    #variables importantes
    mid_ind = tamaño //2

    #donde ocurre la magia
    print(lista)

    numero_buscar = int(input("ingresar el numero que desea encontrar: "))

    if numero_buscar == lista[mid_ind]:
        print(f"el numero {numero_buscar} se encuentra en la posicion {mid_ind}")

    elif numero_buscar > lista[mid_ind]:
        resp = busqueda_binaria_max(lista, mid_ind, numero_buscar)
        print(f"el numero {numero_buscar} esta en la posicion {resp}")
    elif numero_buscar < lista[mid_ind]:
        resp = busqueda_binaria_min(lista, mid_ind, numero_buscar)
        print(f"el numero {numero_buscar} esta en la posicion {resp}")


principal()