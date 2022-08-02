__author__ = 'Cátedra de AED'

import otro

def test():
    # crear el vector de conteo...
    n = 1000
    c = n * [0]

    # cargar y contar los números...
    num = int(input('Ingrese un valor entre 0 y 99 (con –1 corta): '))
    while num != -1:
        if 0 <= num < n:
            c[num] += 1
        else:
            print('Error... el número debía ser >= 0 y <', n)

        num = int(input('Ingrese otro valor entre 0 y 99 (con –1 corta): '))

    # mostrar los resultados...
    print('Resultados:')
    for i in range(n):
        if c[i] != 0:
            print('Número', i, '- Frecuencia de aparición', c[i])


if __name__ == '__main__':
    test()
