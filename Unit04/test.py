def validar_cuit(cuit):
    # CUIT: un texto compuesto por 13 números
    # separados por guiones de la siguiente manera: 00-00000000-0
    valido = False
    cant_numeros = 0
    if len(cuit) == 13:
        if cuit[2] == '-' and cuit[11] == '-':
            for car in cuit:
                if car in '0123456789':
                    cant_numeros += 1
            # Controlo si todos los que no son guiones, son digitos
            if cant_numeros == 11:
                valido = True
    return valido


cuit = input('Ingrese un cuit')

hola = validar_cuit(cuit)
print(hola)
