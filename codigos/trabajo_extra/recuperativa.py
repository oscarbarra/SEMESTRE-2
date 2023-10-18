class Recuperatorio:
    def __init__(self):
        self.lista = []
        self.lista_ordenada = False

    def rellenar_lista(self, tam):
        while len(self.lista) < tam:
            num = input("ingresar un numero entero: ")

            try:
                int(num) #revisa si el valor ingresado se puede transformar en entero
                self.lista.append(int(num))

            except ValueError:
                print("lo sentimos el valor ingresado no es un numero entero")

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

        self.lista_ordenada = True


    def linear_search(self, search_num):
        lista_ind = []
        if search_num in self.lista:
            for i  in range(0, len(self.lista)):
                 if self.lista[i] == search_num:
                     lista_ind.append(i)

            print(f"el numero {search_num} esta en los indices:", end=" ")
            for j in range(0, len(lista_ind)):
                print(f"{lista_ind[j]}", end=" ")

        else:
            print(f"lo sentimos el numero {search_num} no pertenece a la lista")


    def interfaz(self):
        while True:
            print("-----------------------------------------------------------------------------------------------")
            print("0:temino programa  /  1:crear_lista  /  2:ordenar_lista  /  3:buscar_numero")
            print("-----------------------------------------------------------------------------------------------\n")
            opcion = (input("ingresar una opcion: "))

            if opcion == "":
                print("porfavor ingresar una de las opciones\n")

            elif opcion.isalpha():
                print("porfavor ingresar una de las opciones\n")

            elif int(opcion) not in [0, 1, 2, 3]:
                print("porfavor ingresar una de las opciones\n")

            elif int(opcion) == 0:
                print("termino del programa")
                break

            elif int(opcion) == 1:
                self.lista = []
                self.lista_ordenada = False
                self.rellenar_lista(int(input("ingrese la cantidad maxima de NUMEROS ENTEROS que aceptara la lista: ")))
                print("\nla lista creada es:")
                self.mostrar_lista()
                input("\n")

            elif int(opcion) == 2:
                self.select_sort()
                print("\nla lista ordenada es:")
                self.mostrar_lista()
                input("\n")

            elif int(opcion) == 3:
                if self.lista_ordenada:
                    self.linear_search(int(input("ingresar el numero a buscar: ")))
                    input("")
                else:
                    print("accion invalida, la lista no esta ordenada\n")
                    input("")


    def mostrar_lista(self):
        print(self.lista)


p1 = Recuperatorio()
p1.interfaz()