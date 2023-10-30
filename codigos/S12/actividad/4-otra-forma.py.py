def sumar_numeros(numero):
    if numero > 0:
        return numero +sumar_numeros(numero-1)
    else:
        return 0
    
numero = int(input("ingresar un numero NATURAL: "))
print(f"la suma de los numeros que estan antes que el {numero} es de: {sumar_numeros(numero)}")