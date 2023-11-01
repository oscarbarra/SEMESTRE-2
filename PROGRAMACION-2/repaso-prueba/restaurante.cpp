#include <iostream>
#include <vector>

class Persona
{
    public:
    std::string nombre;

    Persona(std::string nombre) : nombre(nombre) {}
};

class Restaurante
{
    private:
    int filas = 10;
    int columnas = 10;
    int id = 0;

    public:
    //filas , columnas
    int mesas[10][10];
    //filas * columnas
    int reservas[100]; //almacena el id de la persona que hizo la reservacion

    std::vector <std::string> platillos;
    

    void cantidad_mesas()
    {
        for (int i=0; i<filas; i++)
        {
            for (int j=0; j<columnas; j++)
            {
                mesas[i][j] = 0;
            }
        }
    }

    void reservar_mesa(std::string nombre, int f, int c)
    {
        if (mesas[f-1][c-1] != 0)
        {
            std::cout << nombre << " lo sentimos pero esa mesa ya esta ocupada" << std::endl;
        }

        else if (mesas[f-1][c-1] == 0)
        {
            id++;
            mesas[f-1][c-1] = id;
            reservas[id-1] = id;
        }
    }

    void mostrar_mesas()
    {
        for (int i=0; i<filas; i++)
        {
            for (int j=0; j<columnas; j++)
            {
                std::cout << mesas[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    void mostrar_reservas()
    {
        if (id == 0)
        {
            std::cout << "no hay reservaciones" << std::endl;
        }
        else if (id != 0)
        {
            for (int i=0; i<id; i++)
            {
                if (i+1 % 11 == 0)
                { 
                    std::cout << reservas[i] << std::endl;
                }
                else
                {
                    std::cout << reservas[i] << " ";
                }
            }
        }
    }

    void agregar_patillo(std::string platillo)
    {
        platillos.push_back(platillo);
    }

    void mostrar_carta()
    {
        size_t tam = size(platillos);
        for (int i=0; i<tam; i++)
        {
            std::cout << i << " " << platillos.at(i) << std::endl;
        }
    }
};


int main()
{
    //instancio a los objetos/personas
    Persona p1("oscar");
    Persona p2("felipe");
    Persona p3("florencia");
    Persona p4("cony");

    //intancio al objeto/restaurante
    Restaurante m1;

    //creo la cantidad de mesas
    std::cout << "estado del restaurante" << std::endl;
    m1.cantidad_mesas();
    m1.mostrar_mesas();
    std::cout << std::endl;

    //defino la carta del restaurante
    m1.agregar_patillo("arroz");
    m1.agregar_patillo("tallarines");
    m1.agregar_patillo("lentejas");

    //muetro la carta
    std::cout << "platillos disponibles" << std::endl;
    m1.mostrar_carta();
    std::cout << std::endl;

    //los clientes hacen sus reservaciones
    m1.reservar_mesa(p1.nombre, 2, 5);
    m1.reservar_mesa(p2.nombre, 3, 9);
    m1.reservar_mesa(p3.nombre, 10, 4);
    m1.reservar_mesa(p4.nombre, 7, 6);

    //muestro el estado del restaurante
    std::cout << "estado del restaurante" << std::endl;
    m1.mostrar_mesas();
    std::cout << std::endl;

    //muestra los id de reservacion
    std::cout << "los id de reservados" << std::endl;
    m1.mostrar_reservas();
    return 0;
}