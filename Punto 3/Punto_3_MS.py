import numpy as np
import time
# Programa en Python para la implementación de MergeSort
def fusionar(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Crea arreglos temporales
    L = [0] * (n1)
    R = [0] * (n2)

    # Copia los datos a los arreglos temporales L[] y R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Fusiona los arreglos temporales de vuelta en arr[l..r]
    i = 0  # Índice inicial del primer subarreglo
    j = 0  # Índice inicial del segundo subarreglo
    k = l  # Índice inicial del subarreglo fusionado

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copia los elementos restantes de L[], si los hay
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copia los elementos restantes de R[], si los hay
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l es el índice izquierdo y r es el índice derecho del
# subarreglo de arr que se va a ordenar

def mergeSort(arr, l, r):
    if l < r:

        # Igual a (l+r)//2, pero evita desbordamiento para
        # valores grandes de l y h
        m = l + (r - l) // 2

        # Ordena las mitades izquierda y derecha
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        fusionar(arr, l, m, r)

# Arreglo de 10 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10).tolist()
n = len(arr)
print("El arreglo dado es: ")
for i in range(n):
    print(arr [i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time()
print("\n\nEl arreglo ordenado es")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n\nTiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 50 elementos con valores aleatorios
arr = np.random.randint(0, 100, 50).tolist()
n = len(arr)
print("El arreglo dado es: ")
for i in range(n):
    print(arr [i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time()
print("\n\nEl arreglo ordenado es")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n\nTiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 100 elementos con valores aleatorios
arr = np.random.randint(0, 100, 100).tolist()
n = len(arr)
print("El arreglo dado es: ")
for i in range(n):
    print(arr [i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time()
print("\n\nEl arreglo ordenado es")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n\nTiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 500 elementos con valores aleatorios
arr = np.random.randint(0, 100, 500).tolist()
n = len(arr)
print("El arreglo dado es: ")
for i in range(n):
    print(arr [i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time()
print("\n\nEl arreglo ordenado es")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n\nTiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 1000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 1000).tolist()
n = len(arr)
print("El arreglo dado es: ")
for i in range(n):
    print(arr [i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time()
print("\n\nEl arreglo ordenado es")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n\nTiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 2000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 2000).tolist()
n = len(arr)
print("El arreglo dado es: ")
for i in range(n):
    print(arr [i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time()
print("\n\nEl arreglo ordenado es")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n\nTiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 5000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 5000).tolist()
n = len(arr)
print("El arreglo dado es: ")
for i in range(n):
    print(arr [i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time()
print("\n\nEl arreglo ordenado es")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n\nTiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 10000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10000).tolist()
n = len(arr)
print("El arreglo dado es: ")
for i in range(n):
    print(arr [i], end=" ")
start_time = time.time()
mergeSort(arr, 0, n-1)
end_time = time.time()
print("\nEl arreglo ordenado es")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\nTiempo de ejecución:", end_time - start_time, "segundos")



