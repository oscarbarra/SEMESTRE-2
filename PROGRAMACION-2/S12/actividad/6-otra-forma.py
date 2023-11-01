def binario_a_decimal(binario, exponente):
    if len(binario) == 0:
        return 0
    else:  #FORMULA:  X0 *2^0 + X1 *2^1 + X2 *2^2 + ....
        return binario_a_decimal(binario[ : len(binario) -1], exponente +1) +int(binario[len(binario) -1]) *pow(2, exponente)

binario = input("ingresar un numero BINARIO: ") #se deja como string para poder iterar
exponente = 0
print(f"el numero binario {binario} en decimal es: {binario_a_decimal(binario, exponente)}")