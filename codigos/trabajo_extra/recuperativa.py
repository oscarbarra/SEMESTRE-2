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

    def mostrar_lista(self):
        print(self.lista)


p1 = Nombre(int(input("cantidad de numeros a agregar: ")))

p1.mostrar_lista()

p1.select_sort()

p1.mostrar_lista()