#include <iostream>

int sumarNumeros(int numero);

int main()
{

    int numero;
    std::cout << "ingresar un numero NATURAL: "; std::cin >> numero;

    std::cout << "la suma de los numeros antes del " << numero << " es de: " << sumarNumeros(numero) << std::endl;

    return 0;
}

int sumarNumeros(int numero)
{
    if (numero <= 0){
        return 0;
    } 
    else if(numero >= 1){
        return numero + sumarNumeros(numero -1);
    }
    return 0;
};