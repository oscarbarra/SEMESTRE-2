import time


#big(o) = n*log(n)
def merge_sort(lista):
    #caso base // detiene la recursividad
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]

        #caso recursivo // divide la lista hasta que que 'len == 1'
        merge_sort(left)
        merge_sort(right)


        #ordena la lista
        i = j = k = 0
        #i = left
        #j = right
        #k = comodin

        #compara los tamaños hasta que uno de los arreglos se queda vacio
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

    return

mi_lista = [i for i in range(10000, 0, -1)]  # Creamos una lista con un millón de elementos en orden inverso

start_time = time.time()
merge_sort(mi_lista)
end_time = time.time()

print(f"El tiempo de ejecución fue de {end_time - start_time} segundos")