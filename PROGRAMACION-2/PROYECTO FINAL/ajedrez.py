import tkinter as tk

class App():
    def __init__(self, L_CUADRADO):
        self.L_CUADRADO = L_CUADRADO

        self.ventana = tk.Tk()
        self.ventana.title("ajedrez")
        self.ventana.geometry(f"{str(L_CUADRADO *15)}x{str(L_CUADRADO *10)}")

        self.interfaz = tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def dibujarTablero(self):
        #self.interfaz.create_rectangle(x0, y0, x1, y1, fill=)
        for f in range(15):
            for c in range(10):
                if (f+c) %2 == 0:
                    self.interfaz.create_rectangle(f *self.L_CUADRADO, c *self.L_CUADRADO, (f +1) *self.L_CUADRADO, (c +1) *self.L_CUADRADO, fill="#dfc07f")
                else:
                    self.interfaz.create_rectangle(f *self.L_CUADRADO, c *self.L_CUADRADO, (f +1) *self.L_CUADRADO, (c +1) *self.L_CUADRADO, fill="#7a4f37")
ajedrez = App(70)
ajedrez.dibujarTablero()

ajedrez()