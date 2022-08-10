def buscar_temperatura(regiones, temperaturas, region, x):
    existe = False
    for i in range(len(regiones)):
        if regiones[i] == region and temperaturas[i] > x:
            existe = True
            break

    return existe


# elif op == 4:
#     reg = int(input("Ingrese región a analizar: "))
#     x = int(input("Ingrese temperatura a controlar: "))
#     existe = buscar_temperatura(regiones, temperaturas, reg, x)
#     if existe:
#         resultado = "Hay al menos una temperatura menor a"
#     else:
#         resultado = "No hay temperaturas menores a"
#     print(resultado, x, "en la región analizada")
