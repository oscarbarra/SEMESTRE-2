def decimal_a_binario(numero):
    if numero < 2 and numero >= 0:
        return str(numero)
    else:
        return decimal_a_binario(numero //2) + str(numero %2)

numero = int(input("ingresar un numero NATURAL: "))
print(f"el numero {numero} en binario es: {decimal_a_binario(numero)}")