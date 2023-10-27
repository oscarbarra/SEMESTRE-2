def sumar_numeros_pares(num, resultado):
    if num % 2 == 0 and num >= 2:
        resultado.append(num)
        sumar_numeros_pares(num-2, resultado)
        
    elif num !=0 and num % 2 == 1:
        print(f"el numero {num} no es par")
    
    return sum(resultado)


num = int(input("ingresar un numero NATURAL: "))
resultado = []

print(f"la suma de los numeros antes del {num} es: {sumar_numeros_pares(num, resultado)}")