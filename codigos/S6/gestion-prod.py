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
    def __init__(self, nombre, precio, categoria, tipo):
        super().__init__(nombre, precio, categoria)
        self.tipo = tipo

    def mostrar_prod(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}")
        print(f"categoria: {self.categoria}\ntipo: {self.tipo}")

class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, tipo):
        super().__init__(nombre, precio, categoria)
        self.tipo = tipo

    def mostrar_prod(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}")
        print(f"categoria: {self.categoria}\ntipo: {self.tipo}")


E1 = Electronico("pc", 1000, "Electronico", "gamer")
A1 = Alimento("arroz", 1000, "alimento", "cereal")
V1 = Vestimenta("polera", 5000, "Vestimenta", "verano")


for i in (E1, A1, V1):
    i.mostrar_prod()
    print("\n")
    
