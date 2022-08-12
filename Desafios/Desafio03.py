
import soporte
'''
En esta consigna se propone resolver el mismo problema del Conteo de Frecuencias, pero ahora partiendo de un vector de números que se sabe que están en un rango o intervalo conocido, y que además ese intervalo es razonable para ser mapeado en una estructura de datos de memoria.

Si este es el caso (se conoce el rango o intervalo de los valores de entrada) entonces se puede plantear una solución MUCHO más rápida que la que vimos en las consignas 1, 2 y 3: en lugar de usar dos arreglos para almacenar y contar los números que van apareciendo, y tener que buscar secuencialmente cada número x en el arreglo de números, podemos usar (ahora sí...) un arreglo de conteo directo. La idea es crear un arreglo c de tantos elementos como números posibles haya en el rango de entrada (300000 casilleros en nuestro caso), y usar a cada casillero c[x] para contar la cantidad de veces que entró el número x.  Esta solución requiere eventualmente más memoria (ya que podrían quedar casilleros sin usar en el arreglo c), pero a cambio es notablemente más veloz (y garantizamos que los alumnos notarán esto cuando comparen los tiempos de ejecución de las dos soluciones...)

El algoritmo básico general podría ser el siguiente, suponiendo que el rango o intervalo de los valores de entrada es [0..299999] (como dijimos) y lo que se pide es determinar cuántos números diferentes entraron:

0.)  Cree un arreglo c de 300000 casillas, inicializadas en cero.
1.)  Para cada número x del vector v de entrada:
          1.1) Incremente en uno la casilla c[x]
2.)  Mostrar la cantidad de casilleros diferentes de cero que quedaron en el arreglo c.

Para cumplir con las consignas que quedan, debe usar el mismo módulo soporte.py que ya se indicó para las consignas anteriores (programado por los docentes de la Cátedra) pero de forma que ahora se use la función que corresponda para generar un arreglo con valores en un intervalo conocido, de acuerdo a los siguientes pasos generales:

a.) En el mismo proyecto que ya ha creado para las consignas anteriores, en el que ya debería estar incluido el módulo soporte.py, cree otro programa e importe el módulo soporte.py (o añada la nueva funcionalidad al programa que ya desarrolló para las consignas anteriores). Haga lo que haga, sólo asegúrese de importar el módulo soporte.py como se indicó.

b.) Su programa debe usar ahora la función soporte.vector_known_range() (no se confunda: ahora se llama vector_known_range() en lugar de vector_unknown_range()) para crear y obtener el vector v que debe procesar. El vector debe generarse con n = 300000 (trescientos mil) elementos, y la instrucción que le permitiría hacerlo es simplemente la siguiente:

v = soporte.vector_known_range(300000)

c.) La instrucción anterior, asignará en v una referencia a un arreglo con n = 300000 números mayores o iguales a 0, que pueden venir repetidos, pero de forma que ahora todos los números del vector están en el intervalo [0..299999]. La invocación v = soporte.vector_known_range(300000) creará exactamente el mismo arreglo cada vez que la ejecute, por lo que no debe preocuparse: sus datos serán siempre los mismos, siempre y cuando el parámetro sea 300000. Con otros valores de ese parámetro, el vector generado será diferente: asegúrese de invocar a la función pasando el valor 300000 como parámetro.

d.) En el mismo programa, implemente el algoritmo de conteo descripto en el pseudocódigo presentado más arriba, y obtenga como primera medida, la cantidad de números diferentes que detecte en el vector v de entrada.

Registre ahora (en el casillero que sigue) la cantidad de números diferentes del nuevo archivo de entrada provisto:
'''


def process(v, c):
    for i in range(len(v)):
        c[v[i]] += 1
    return c


def numerosDif(cResuelta):
    arraySin0 = []
    contadorManual = 0
    for i in range(len(cResuelta)):
        if cResuelta[i] != 0:
            contadorManual += 1
            arraySin0.append(cResuelta[i])
    return contadorManual, arraySin0


def main():
    modal = 0
    c = [0] * 300000
    v = soporte.vector_known_range(300000)
    cResuelta = process(v, c)
    contadorCeros,  arraySin0 = numerosDif(cResuelta)


main()
