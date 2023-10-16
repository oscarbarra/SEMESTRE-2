#cositas importantes
#crear lista/ ordenar lista/ buscar numero

class Nombre:
    def __init__(self, tam):
        self.lista = [int(input("ingresar un numero: ")) for i in range(tam)]

    def select_sort(self):
        ciclo = 0
        for i in range(0, len(self.lista)):
            aux = i
            ciclo +=1
            for j in range(i+1, len(self.lista)):
                if self.lista[aux] > self.lista[j]:
                    aux = j
            self.lista[i], self.lista[aux] = self.lista[aux], self.lista[i]

            print(f"en el ciclo {ciclo} se van a intercambiar los indices", end=" ")
            print(f"{i}, {aux} que tienen los valores {self.lista[i]}, {self.lista[aux]}")

    def binary_serch(self):
        number_to_serch = int(input("ingresar el numero a buscar: "))
        low=0
        high=len(self.lista)-1
        mid=0
        while low <= high :
            mid = (high + low)//2
            if self.lista[mid] < number_to_serch :
                low = mid + 1
            elif self.lista[mid] > number_to_serch: #buscar hacer que mustre los ind del num repetido
                high = mid - 1 
            else:
                print(f"el numero {number_to_serch} se encuentra en la posicion {mid}")
                return mid
        return

    def mostrar_lista(self):
        print(self.lista)


print("creacion de la lista")
p1 = Nombre(int(input("cantidad de numeros a agregar: ")))
input("")

print("lista creada")
p1.mostrar_lista()
input("")

print("ordenamiento de la lista")
p1.select_sort()
input("")

print("lista ordenada")
print(p1.lista)
input("")

print("buscar numero indicado")
p1.binary_serch()
