#Supongamos que estás en un país con un sistema monetario peculiar. Las denominaciones de las monedas no son las habituales
#y te enfrentas a la tarea de hacer cambio para una cantidad específica.

#El problema es el siguiente: Dado un conjunto de monedas con diferentes denominaciones y una cantidad total, 
#encuentre el número mínimo de monedas que suman esa cantidad. Si no es posible hacer la cantidad con las monedas dadas,
#devuelve -1.

#Ejemplo: Si las monedas son [1, 2, 5] y la cantidad es 11, la respuesta es 3 porque 11 = 5 + 5 + 1.

#HACER DE FORMA DINAMICA
def buscar_combinacion_monedas(monedas, monedas_usadas, total, indice):
    while sum(monedas_usadas) < total:
        if sum(monedas) + monedas[indice] <= total:
            monedas_usadas.append(monedas[indice])
        else:
            indice -=1



monedas = [1, 2, 5, 10, 20]
monedas_usadas = []
total = int(input("ingresar la cantidad de dinero que necesitas: "))
indice = len(monedas)-1

print(indice)

buscar_combinacion_monedas(monedas, monedas_usadas, total, indice)

print(monedas_usadas)