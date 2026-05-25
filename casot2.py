
import random


def promedioMultiplos3(lst):
    return recorrerlista(lst, 0, None, None)


def recorrerlista(lst, x, menor, mayor):

    if x == len(lst):

        if menor == None:
            return 0
        
        return (menor + mayor) / 2

    else:

        if lst[x] % 3 == 0:

            if menor == None or lst[x] < menor:
                menor = lst[x]

            if mayor == None or lst[x] > mayor:
                mayor = lst[x]

        return recorrerlista(lst, x+1, menor, mayor)


tam = int(input("Ingrese tamaño del arreglo: "))

lista = []

for i in range(tam):

    num = random.randint(10, 9999)

    lista.append(num)


print("Arreglo generado:")
print(lista)

print("Promedio:", promedioMultiplos3(lista))