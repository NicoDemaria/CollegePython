lista = [3, 5, 2, 1, 10]


def mesSeco(lluviasanuales):
    min = 0
    for i in range(len(lluviasanuales)):
        if lluviasanuales[i] < lluviasanuales[min]:
            min = i
            print(min)

    return min


print(mesSeco(lista))
