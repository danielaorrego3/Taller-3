import numpy as np
import time
def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

# Arreglo de 10 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10).tolist()
print("Arreglo no ordenado")
print(arr)
stat_time = time.time()
insertionSort(arr)
end_time = time.time()
print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - stat_time, "segundos")

# Arreglo de 50 elementos con valores aleatorios
arr = np.random.randint(0, 100, 50).tolist()
print("Arreglo no ordenado")
print(arr)
stat_time = time.time()
insertionSort(arr)
end_time = time.time()
print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - stat_time, "segundos")

# Arreglo de 100 elementos con valores aleatorios
arr = np.random.randint(0, 100, 100).tolist()
print("Arreglo no ordenado")
print(arr)
stat_time = time.time()
insertionSort(arr)
end_time = time.time()
print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - stat_time, "segundos")


# Arreglo de 500 elementos con valores aleatorios
arr = np.random.randint(0, 100, 500).tolist()
print("Arreglo no ordenado")
print(arr)
stat_time = time.time()
insertionSort(arr)
end_time = time.time()
print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - stat_time, "segundos")

# Arreglo de 1000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 1000).tolist()
print("Arreglo no ordenado")
print(arr)
stat_time = time.time()
insertionSort(arr)
end_time = time.time()
print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - stat_time, "segundos")

# Arreglo de 2000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 2000).tolist()
print("Arreglo no ordenado")
print(arr)
stat_time = time.time()
insertionSort(arr)
end_time = time.time()
print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - stat_time, "segundos")

# Arreglo de 5000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 5000).tolist()
print("Arreglo no ordenado")
print(arr)
stat_time = time.time()
insertionSort(arr)
end_time = time.time()
print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - stat_time, "segundos")

# Arreglo de 10000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10000).tolist()
print("Arreglo no ordenado")
print(arr)
stat_time = time.time()
insertionSort(arr)
end_time = time.time()
print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - stat_time, "segundos")




