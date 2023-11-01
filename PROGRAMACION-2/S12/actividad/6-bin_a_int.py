def binario_a_decimal(num, lista, indice, exponente):
    if indice > -1:
        lista.append(int(num[indice]) *pow(2, exponente))
        binario_a_decimal(num, lista, indice -1, exponente +1)

    return sum(lista)

num = (input("ingresar un numero BINARIO: "))
indice = len(num)-1
exponente = 0
lista = [] #almacena los numeros de la operacion // num * 2^exponente

print(f"el numero binario {num} escrito en el sistema decimal es {binario_a_decimal(num, lista, indice, exponente)}")