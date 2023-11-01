def sort_list(lista, indice):
    if indice < len(lista):
        for i in range(indice +1, len(lista)):
            if lista[i] < lista[indice]:
                lista[i], lista[indice] = lista[indice], lista[i]

        sort_list(lista, indice +1)

    return lista


lista = [i for i in range(20, 0, -1)]
indice = 0

print(f"la lista ordenada es:\n{sort_list(lista, indice)}")