def partition(arr, low, high):
    pivot = arr[high]   # Tomamos el último elemento como pivot
    i = (low - 1)       # índice del elemento más pequeño

    for j in range(low, high):
        # Si el elemento actual es más pequeño o igual al pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambio

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Intercambio el pivot
    return (i + 1) #indice final del pivot

def quick_sort(arr, low, high):
    if low < high:
        # pi es el índice de particionamiento//indice final del pivot
        pi = partition(arr, low, high)

        # Ordenar separadamente los elementos antes y después del índice de particionamiento
        quick_sort(arr, low, pi - 1) #izq 
        quick_sort(arr, pi + 1, high) #der

# Código de prueba
arr = [i for i in range(100, 0, -1)]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("El arreglo ordenado es:", arr)