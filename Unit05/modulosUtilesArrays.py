i = 0
n = 0
# TODO ordenadar un arreglo de mayor a menor
for j in range(i+1, n):
    v = []
    if v[i] > v[j]:
        v[i], v[j] = v[j], v[i]


def selection_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

# TODO búsqueda secuencial
