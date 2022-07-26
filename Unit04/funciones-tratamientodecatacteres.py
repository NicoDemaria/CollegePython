# módulo con funciones para procesamiento de caracteres

def es_digito(car):
    res = False

    if car in "0123456789":
        res = True

    return res


def es_vocal(car):
    res = False

    if car.lower() in "aeiouáéíóúü":
        res = True

    return res


def es_consonante(car):
    res = False

    if car.lower() in "bcdfghjklmnñpqrstvwxyz":
        res = True

    return res


def es_letra(car):
    res = False

    if es_vocal(car) or es_consonante(car):
        res = True

    return res


def es_mayuscula(car):
    res = False

    if car in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        res = True

    return res


def prueba():
    print(es_vocal("A"))
    print(es_vocal("g"))
    print(es_consonante("T"))
    print(es_consonante("e"))
    print(es_letra("Y"))
    print(es_letra("-"))
    print(es_mayuscula("A"))
    print(es_mayuscula("a"))


# script principal
if __name__ == '__main__':
    prueba()


# módulo con funciones para procesamiento de caracteres
def es_digito(car):
    return car in "0123456789"


def es_vocal(car):
    return car.lower() in "aeiouáéíóúü"


def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


def es_letra(car):
    return es_vocal(car) or es_consonante(car)


def es_mayuscula_v1(car):
    return car in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def es_mayuscula_v2(car):
    return es_letra(car) and car == car.upper()
