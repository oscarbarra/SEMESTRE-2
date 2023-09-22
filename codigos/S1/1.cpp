#include <iostream>

//ordenar una lista con un metodo de ordenamiento de nuestra eleccion

//definicion de las constantes
const int tamano = 10;


//mencion de las funciones prototipo
void mostrar_lista (int [tamano], int);
void select_sort(int [tamano], int);


int main(){
    //creo un array
    int lista[tamano] = {9,8,7,6,5,4,3,2,1,0};

    //determino el tamaño del array
    int len = sizeof(lista) / sizeof(lista[0]);

    mostrar_lista(lista, len);
    select_sort(lista, len);
    mostrar_lista(lista, len);

    return 0;
}


void select_sort(int lista[tamano], int len){
    for (int i=0; i<len; i++){
        int indice_aux = i;
        for (int j=i+1; j<len; j++){
            if (lista[indice_aux] > lista[j]){
                indice_aux = j;
            }
        }
        std::swap(lista[indice_aux], lista[i]);
    }
}


void mostrar_lista(int lista[tamano], int len){
    for (int i=0; i<len; i++){
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;
}