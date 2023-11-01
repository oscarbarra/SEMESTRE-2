def sumar_numeros_pares(numero):
    if numero >= 0 and numero %2 == 0:
        return numero +sumar_numeros_pares(numero -2)
    elif numero %2 == 1:
        return f"\nel numero {numero} no es par"
    else:
        return 0
    
numero = int(input("ingresar un numero NATURAL PAR: "))
print(f"la suma de los numeros pares es de: {sumar_numeros_pares(numero)}")