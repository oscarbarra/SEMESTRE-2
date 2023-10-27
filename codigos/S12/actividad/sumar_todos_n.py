def sumar_numeros(num, resultado):
    if num > 0:
        resultado.append(num)
        sumar_numeros(num-1, resultado)
        
    return sum(resultado)


num = int(input("ingresar un numero NATURAL: "))
resultado = []

print(f"la suma de los numeros antes del {num} es: {sumar_numeros(num, resultado)}")