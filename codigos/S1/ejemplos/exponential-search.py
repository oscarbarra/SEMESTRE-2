
def bin_search(list, search):
    while True:
        #actualizacion de los valores clave
        min_ind = 0
        mid_ind = len(list) // 2
        max_ind = len(list)

        print(f"min: {list[mid_ind]}, mid: {list[mid_ind]}, max: {list[max_ind-1]}")

        if max_ind == 1 and list[min_ind] == search:
            print(f"el numero {search} esta en la pos {min_ind}")
            break

        elif max_ind == 1 and list[min_ind] != search:
            print(f"el numero {search} no pertenece a la lista")
            break

        elif list[mid_ind] == search:
            print(f"el numero {search} esta en la pos {mid_ind}")
            break

        elif mid_ind > search:
            max_ind = mid_ind
            list = list[min_ind : max_ind]

        elif mid_ind < search:
            min_ind = mid_ind
            list = list[min_ind : max_ind]
    return

def exponential_search(list, search):
    auxiliar = 1
    min_ind = 0
    max_ind = len(list)

    while auxiliar < max_ind:
        if list[0] == search:
            print(f"el numero {search} esta en la pos {0}")
            break

        elif list[auxiliar] >= search:
            max_ind = auxiliar+1
            break

        elif list[auxiliar] <= search:
            min_ind = auxiliar
            auxiliar +=auxiliar
    
    bin_search(list[min_ind : max_ind], search)
    return

#creacion de la lista
list = [i for i in range(0, 10000)]
#llamada a la funcion principal
exponential_search(list, 156)