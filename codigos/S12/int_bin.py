def resto(numero, lista):
    if numero >= 2:
        lista.append(numero %2)
        numero = numero //2
        resto(numero, lista)
    else:
        lista.append(numero)

    return lista

def num_binario(numero, lista):
    binario = "0"
    concatenar = resto(numero, lista)

    for i in range(len(lista)-1, -1, -1):
        binario += str(concatenar[i])

    return binario


lista =[]
numero = int(input())

print(num_binario(numero, lista))