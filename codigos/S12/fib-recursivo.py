import time
import matplotlib.pyplot as plt

#algoritmos de fibonashi
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

x1 = [0, fib_recursivo(int(input("ingresar un numero NATURAL: ")))]

end_time = time.time()

y1 = [0, end_time - star_time]

print(f"valor n {x1[1]},  tiempo de ejecucion {y1[1]}")

plt.ticklabel_format(style="plain")
plt.plot(x1, y1, label="recursivo")
plt.xlim(0, x1[1])
plt.ylim(0, y1[1])

plt.title("Tiempo de ejecucion: Fibonacci recursivo")
plt.xlabel("valor de n")
plt.ylabel("tiempo de ejecucion")

plt.legend(loc = "upper left")
plt.grid()
plt.show()