class Producto:
    def __init__(self, nombre, precio, categotia):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categotia

class Electronico(Producto):
    def __init__(self,nombre, precio, categoria, tipo):
        super().__init__(nombre, precio, categoria)
        self.tipo = tipo

    def mostrar_prod(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}")
        print(f"categoria: {self.categoria}\ntipo: {self.tipo}")

class Alimento(Producto):
    def __init__(self, nombre, precio, categoria, nacional):
        super().__init__(nombre, precio, categoria)
        self.prod_nacional = nacional

    def mostrar_prod(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}")
        print(f"categoria: {self.categoria}\nnacional: {self.prod_nacional}")

class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, temporada):
        super().__init__(nombre, precio, categoria)
        self.temporada = temporada

    def mostrar_prod(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}")
        print(f"categoria: {self.categoria}\ntemporada: {self.temporada}")


E1 = Electronico("pc", 1000, "Electronico", "gamer")
A1 = Alimento("arroz", 1000, "alimento", "no")
V1 = Vestimenta("polera", 5000, "Vestimenta", "verano")


for i in (E1, A1, V1):
    i.mostrar_prod()
    print("\n")
    
