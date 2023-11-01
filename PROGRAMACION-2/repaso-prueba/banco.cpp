//banco abrir y cerrar cuentas, depositar y sacar plata

#include <iostream>
#include <vector>

class Persona
{
    public:
    //atributo
    std::string nombre;

    //constructor 
    Persona (std::string nombre) : nombre(nombre) {}
};

class Banco
{
    private:
    std::vector <int> saldos;
    std::vector <std::string> clientes;

    public:

    void crear_cuenta(std::string nombre, int saldo_inicial=0)
    {
        if (saldo_inicial == 0)
        {
            saldos.push_back(saldo_inicial);
            clientes.push_back(nombre);
        }

        else
        {
            saldos.push_back(saldo_inicial);
            clientes.push_back(nombre);
        }
    }

    void eliminar_cuenta(std::string nombre)
    {
        size_t tam = size(clientes);

        for (int i=0; i<tam; i++)
        {
            if (clientes.at(i) == nombre)
            {
                clientes.at(i) = "vacio";
                saldos.at(i) = 0;
            }
        }
    }

    void agregar_saldo(int id, int saldo_agregar)
    {
        saldos.at(id) += saldo_agregar;
        std::cout << clientes.at(id) << " tu nuevo saldo es de: " << saldos.at(id) << std::endl;
    }

    void sacar_saldo(int id, int saldo_sacar)
    {
        if (saldos.at(id) <= 0)
        {
            std::cout << clientes.at(id) << " accion invalida tu saldo es de: " << 0 << std::endl;
        }

        else if (saldos.at(id) > 0 && saldos.at(id) - saldo_sacar <= 0)
        {
            std::cout << clientes.at(id) << " lo sentimos el monto a sacar " << saldo_sacar << " es demasiado grande" << std::endl;
            std::cout << clientes.at(id) << " actualmente tienes un saldo de: " << saldos.at(id) << std::endl;
        }

        else if (saldos.at(id) > 0 && saldos.at(id) - saldo_sacar >= 0)
        {
            saldos.at(id) -= saldo_sacar;

            std::cout << clientes.at(id) << " te nuevo saldo es de: " << saldos.at(id) << std::endl;
        }
    }

    void mostrar_datos_cliente()
    {
        size_t tam = size(clientes);

        for (int i=0; i<tam; i++)
        {
            if (clientes.at(i) == "vacio")
            {
                std::cout <<"id: " << i << " el cliente elimino su cuenta" << std::endl;
            }

            else
            {
            std::cout <<"id: " << i << " cliente: " << clientes.at(i);
            std::cout <<" saldo: " << saldos.at(i) << std::endl;   
            }
        }
    }
};

int main()
{
    Persona p1("oscar");
    Persona p2("felipe");
    Persona p3("fernando");

    Banco chile;

    chile.crear_cuenta(p1.nombre, 100);
    chile.crear_cuenta(p2.nombre, 200);
    chile.crear_cuenta(p3.nombre);
    chile.mostrar_datos_cliente();
    std::cout << std::endl;

    chile.eliminar_cuenta("oscar");
    chile.mostrar_datos_cliente();
    std::cout << std::endl;

    chile.agregar_saldo(1, 100);
    std::cout << std::endl;

    chile.sacar_saldo(1, 250);
    chile.sacar_saldo(2, 500);


    return 0;
}