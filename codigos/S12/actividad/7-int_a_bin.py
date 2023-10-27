def resto(numero, lista):
    if numero >= 2:
        lista.append(numero %2)
        numero = numero //2
        resto(numero, lista)
    else:
        lista.append(numero)

    return lista

def num_binario(numero, lista):
    binario = ""
    concatenar = resto(numero, lista)

    for i in range(len(lista)-1, -1, -1):
        binario += str(concatenar[i])

    return binario


lista =[]
numero = int(input("ingresar un numero NATURAL: "))

print(f"el numero {numero} en binario es: {num_binario(numero, lista)}")