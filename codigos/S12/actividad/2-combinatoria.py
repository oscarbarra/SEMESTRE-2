#tratando de hacer la combinatoria

def factorial(numero):
    if numero > 0:
        return numero * factorial(numero-1)
    else:
        return 1

def combinatoria(poblacion, muestra, auxiliar):
    return poblacion /(muestra *auxiliar)

n = int(input("ingresar la 'POBLACION': "))
r = int(input("ingresar la 'MUESTRA': "))

#--- n! /(r! *(n-r)!)
print(f"el resultado de la combinatoria es: {combinatoria(factorial(n), factorial(r), factorial(n -r))}")