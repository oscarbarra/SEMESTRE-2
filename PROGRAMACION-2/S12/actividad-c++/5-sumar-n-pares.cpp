#include <iostream>

int sumarNumerosPares(int numero);

int main()
{
    int numero;
    std::cout << "ingresar un numero NATURAL PAR: ";std::cin >> numero;

    std::cout << sumarNumerosPares(numero) << std::endl;

    return 0;
}

int sumarNumerosPares(int numero)
{
    if (numero %2 == 1 and numero > 0){
        std::cout << "el numero " << numero << " no es par";
    }
    else if(numero %2 == 0 and numero > 0){
        return numero +sumarNumerosPares(numero -2);
    }

    return 0;
}