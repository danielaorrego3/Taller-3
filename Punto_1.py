import numpy as np
import time

def stooge_sort(arr):
    start_time = time.time()
    stooge(arr, 0, len(arr) - 1)
    end_time = time.time()
    print(f"Tiempo de ejecución de stooge_sort: {end_time - start_time} segundos")
    return arr

def stooge(arr, i, h):
    if i >= h:
        return
    if arr[i] > arr[h]:
        arr[i], arr[h] = arr[h], arr[i]
    if h - i + 1 > 2:
        t = int((h - i + 1) / 3)
        stooge(arr, i, (h - t))
        stooge(arr, i + t, (h))
        stooge(arr, i, (h - t))

# Arreglo de 10 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10).tolist()
print("El arreglo es ")
print(arr)
print(stooge_sort(arr))

# Arreglo de 100 elementos con valores aleatorios
arr = np.random.randint(0, 100, 100).tolist()
print("El arreglo es ")
print(arr)
print(stooge_sort(arr))

# Arreglo de 1000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 1000).tolist()
print("El arreglo es ")
print(arr)
print(stooge_sort(arr))

# Arreglo de 10000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10000).tolist()
print("El arreglo es ")
print(arr)
print(stooge_sort(arr))
