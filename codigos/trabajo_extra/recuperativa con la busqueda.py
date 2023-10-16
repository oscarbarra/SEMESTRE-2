#cositas importantes
#crear lista/ ordenar lista/ buscar numero

class Nombre:
    def __init__(self, tam):
        self.lista = [int(input("ingresar un numero: ")) for i in range(tam)]

    def mostrar_lista(self):
        print(f"la lista es: \n{self.lista}")

    #put in here the serch algoritm
 
    def binary_serch(self):
        number_to_serch = int(input("inserte el numero a buscar siendo un numero entero: "))
        low=0
        high=len(self.lista)-1
        mid=0
        while low <= high :
            mid = (high + low)//2
            if self.lista[mid] < number_to_serch :
                low = mid + 1
            elif self.lista[mid] > number_to_serch:
                high = mid - 1 
            else:
                print(f"the number {number_to_serch} is in the index {mid}")
                return mid
        return -1

p1 = Nombre(int(input("cantidad de numeros a agregar: ")))
p1.mostrar_lista()
p1.binary_serch()

