import matplotlib.pyplot as plt
import time
#import numpy as np

#fibonacci dinamio
def fib_dinamico(lista, indice, num):
    for i in range(indice, num):
        fibonacci = lista[i-1] + lista[i-2]
        lista.append(fibonacci)
        indice +=1
    
    return lista[indice-1]


#fibonacci recursivo
def fib_recursivo(num):
    if num < 0:
        return "fin del codigo"
    elif num == 0:
        return 0
    
    elif num == 1:
        return 1

    elif num > 1:
        return fib_recursivo(num-1) + fib_recursivo(num-2)
    

lista = [0, 1] #fib dinamico
num = int(input("ingresar un numero NATURAL: ")) #variable compartida
indice = 2 #fib dinamico

#fib dinamico
tiempo_dinamico = time.time()
xDinamico = [0, fib_dinamico(lista, indice, num+1)]
final_dinamico = time.time()
yDinamico = [0, final_dinamico - tiempo_dinamico]
print(f"valor de fib dinamico: {xDinamico[1]}")

#fib recursivo
tiempo_recursivo = time.time()
xRescursivo = [0, fib_recursivo(num)]
final_recursivo = time.time()
yRescursivo = [0, final_recursivo - tiempo_recursivo]
print(f"valor de fib recursivo: {xRescursivo[1]}\ntiempo de ejecucion: {yRescursivo[1]}")


plt.ticklabel_format(style='plain') #muetra el numero completo
plt.plot(xDinamico, yDinamico, label="Dinamico") #fib dinamico
plt.plot(xRescursivo, yRescursivo, label="Recursivo") #fib recursivo

plt.xlim(0, xDinamico[1]) #limite del eje x
plt.ylim(-0.5   , yRescursivo[1]+1) #limite del eje y

plt.legend(loc="upper left") #posicion de la leyenda
plt.title("Comparacion Tiempo De Ejecucion: Fibonacci Recursivo vs Dinamico")
plt.xlabel("Valor de n")
plt.ylabel("tiempo de ejecucion (segundos)")

plt.grid() #fondo cuadriculado
plt.show()