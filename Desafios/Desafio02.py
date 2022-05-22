# Por ejemplo, si partimos de n = 13 y aplicamos la relación sucesivamente sobre el último valor calculado, se genera la siguiente secuencia hasta que finalmente se llega al 1: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]. El conjunto de valores así obtenidos, se suele designar como la órbita de n, y el número de iteraciones (que es el tamaño del conjunto de valores obtenidos) hasta alcanzar el 1 partiendo desde n, se suele conocer como la longitud de la órbita de n o también como el tiempo total de parada de n (o el total stopping time de n).

# Su tarea es desarrollar un programa que permita cargar por teclado el valor de n, y luego calcule y muestre todos los valores de la órbita de n, mostrando también (al final) el valor de la longitud de la órbita de n, el promedio entre todos los valores de esa órbita, y el valor que haya sido el mayor de todos en la órbita. Por ejemplo, si se carga n = 13, la salida del programa debería ser la siguiente:

# n = 13

# Orbita de n = 13 (valores calculados incluyendo al 13 y al 1): [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

# Longitud de la órbita (cantidad de valores calculados hasta llegar al 1): 10

# Promedio de todos los valores de la órbita:  11.9

# Mayor de los números en esa órbita:  40


from traceback import print_tb


n = int(input("Ingrese el valor de n: "))
orbita = 1
mayor = 0
lista = []
sumador = 0
while n != 1:
    print(n)
    orbita += 1
    sumador += n
    if n % 2 == 0:
        n = n // 2
        lista.append(n)

    elif n % 2 != 0:
        n = 3 * n + 1
        lista.append(n)
valorMax = max(lista)
promedio = sumador / orbita
print(n)
print('La longitud de la orbita es: ', orbita)
print('El maximo valor es: ', valorMax)
print('El promedio es: ', promedio)
