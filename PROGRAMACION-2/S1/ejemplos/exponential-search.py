def binary_search(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, left, mid-1, x)
        return binary_search(arr, mid+1, right, x)
    return -1

def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= x:
        i = i * 2
    return binary_search(arr, i // 2, min(i, len(arr)-1), x)

# Código de prueba
arr = [i for i in range(1, 10000)]
x = 2
print(f"El número {x} está en el índice {exponential_search(arr, x)}")