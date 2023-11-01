#include <iostream>

//buscar un elemento en una lista ordenada con bin-serch

//INTENTA TERMINAR CUANDO SEPAS MAS DE C++

//defino las constantes
const int tamaño = 10;

//funciones prototipos


int main(){
    //creo la lista
    int lista[tamaño] = {0,1,2,3,4,5,6,7,8,9};

    //tamaño de la lista
    int len = sizeof(lista) / sizeof(lista[0]);

    //adtos importantes para la funcion de busqueda
    int min_ind = 0;
    int mid_ind = len /2;
    int max_ind = len;

    int numero;
    std::cout << "ingresar el numero que desea buscar: " << std::endl; std::cin >> numero;

    //comportamiento del programa

    return 0;
}

