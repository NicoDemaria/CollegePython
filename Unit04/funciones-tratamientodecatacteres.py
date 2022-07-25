# Es una vocal?

def esVocal(car):
    if car in 'aeiouAEIOU':
        return True
    return False


# Es un digito?

def esDigito(car):
    if car in '0123456789':
        return True
    return False

# Es blanco o un punto?


def esTerminador(car):
    if car in '.':
        return True
    return False

# Es una consonante?


def esConsonante(car):
    if car in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        return True
    return False
