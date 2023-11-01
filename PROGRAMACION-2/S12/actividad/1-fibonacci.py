import time

def fib_recursivo(num):
    if num < 0:
        return "fin del codigo" 
    
    elif num == 0:
        return 0
    
    elif num == 1:
        return 1

    elif num > 1:
        return fib_recursivo(num-1) + fib_recursivo(num-2)
    
star_time = time.time()
x1 = fib_recursivo(int(input("ingresar un numero NATURAL: ")))
end_time = time.time()
y1 = end_time - star_time

print(f"valor de la suma es: {x1},  tiempo de ejecucion fue de: {y1}")