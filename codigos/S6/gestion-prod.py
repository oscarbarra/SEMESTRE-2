class Producto:
    def __init__(self, nombre, precio, categotia):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categotia


class Electronico(Producto):
    def __init__(self,nombre, precio, categoria, marca):
        super().__init__(nombre, precio, categoria)
        self.marca = marca

    def mostrar_prod(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}")
        print(f"marca: {self.marca}\ncategoria: {self.categoria}")


class Alimento(Producto):
    def __init__(self, nombre, precio, categoria, procedencia):
        super().__init__(nombre, precio, categoria)
        self.procedencia = procedencia #atributo unico

    def mostrar_prod(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}")
        print(f"procedencia: {self.procedencia}\ncategoria: {self.categoria}")


class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, temporada):
        super().__init__(nombre, precio, categoria)
        self.temporada = temporada #atributo unico

    def mostrar_prod(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}")
        print(f"temporada: {self.temporada}\ncategoria: {self.categoria}")


#inicializacion de los productos
E1 = Electronico("pc", 1000, "Electronico", "LG")
A1 = Alimento("arroz", 1000, "Alimento", "Alemania")
V1 = Vestimenta("polera", 5000, "Vestimenta", "Verano")

#salida de datos
for producto in (E1, A1, V1):
    producto.mostrar_prod()
    input("")