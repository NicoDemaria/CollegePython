''''
Validar si una contrasena especificada por el usuario es segura, para que sea segura:
=> tiene mas de 8 caracteres
=> Tiene al menos una letra mayuscula
=> Tiene al menos un numero

# .isupper() nos devuelve true si todas las letras de un str son mayus pero si hay una miniscula devuelve falso
# .isnumeric()  devuelve si  true si son todos numeros 
'''


def contrasena(password):
    largo = False
    mayus = False
    number = False

    # Comprobar el largo
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            number = True
    if largo and mayus and number:
        return True
    else:
        return False


password = (input('Ingrese su password por favor: '))
verificacion = contrasena(password)

if verificacion:
    print('the password is secure ')
else:
    print('The password is not secure')
