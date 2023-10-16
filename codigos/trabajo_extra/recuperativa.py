#cositas importantes
#crear lista/ ordenar lista/ buscar numero

class Nombre:
    def __init__(self, tam):
        self.lista = [int(input("ingresar un numero: ")) for i in range(tam)]

    def mostrar_lista(self):
        print(self.lista)


p1 = Nombre(int(input("cantidad de numeros a agregar: ")))

p1.mostrar_lista()