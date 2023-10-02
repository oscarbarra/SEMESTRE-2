#haciendo uno de los ejercicios del control

class Libro:
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return  self.nombre


class Biblioteca:
    def __init__(self, *libros):
        self.catalogo = [[i, libros[i]] for i in range(len(libros))]


    def mostrar_catalogo(self, indice="xxx"):
        if indice == "xxx":
            print(self.catalogo)
        else:
            print(self.catalogo[indice])


    def agregar_libro(self, nombre):
        #genera el id del nuevo libro
        new_id = len(self.catalogo)

        #crea un nuevo objeto "nuevo libro"
        new_libro = Libro(nombre)

        self.catalogo.append([new_id, new_libro])


    def buscar_libro(self, buscar):
        #creo lista auxiliar para no modificar la lista principal
        lista_aux = self.catalogo

        #pos_libro alamcenara la posicion en la que se encuentra el libro
        pos_libro = 0

        for i in range (len(lista_aux)):
            if str(lista_aux[i][1]) == buscar:
                pos_libro = i

        #algoritmo de busqueda binaria
        while True:
            mid = len(lista_aux) // 2
            min_value = 0
            max_value = len(lista_aux)

            if str(lista_aux[0][1]) == buscar and max_value == 1:
                print(f"el libro {buscar} tiene id 0 dentro del catalogo")
                break

            if str(lista_aux[mid][1]) == buscar:
                print(f"el libro {buscar} tiene id {pos_libro} dentro del catalogo") 
                break

            elif mid > pos_libro:
                max_value = mid
                lista_aux = lista_aux[min_value : max_value]

            elif mid < pos_libro:
                min_value = mid
                lista_aux = lista_aux[min_value : max_value]

            else:
                print(f"el libro {buscar} no forma parte de nuestro catalogo")
                break


#funcionamiento del programa
#inicializacion de los libros de la biblioteca
L1 = Libro("muerte en el nilo")
L2 = Libro("el pricipito")
L3 = Libro("la bella y la bestia")
L4 = Libro("pinocho")
L5 = Libro("moby dick")

#inicializacion de un empleado que interactua con la biblioteca
E1 = Biblioteca(L1, L2, L3, L4, L5)

print("catalogo inicial")
E1.mostrar_catalogo()
input(" ")

print("agrega el libro oscar al catalogo")
E1.agregar_libro("oscar")
E1.mostrar_catalogo()
input(" ")

print("buscar un libro por el nombre")
E1.buscar_libro(input("ingresar el nombre del libro: "))
input(" ")


#muestra la info del id ingresado
print("buscar un libro por el id")
E1.mostrar_catalogo(int(input("ingresar el id del libro que desea buscar: ")))