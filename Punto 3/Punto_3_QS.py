import numpy as np
import time
# Función para encontrar la posición de partición
def particion(array, bajo, alto):
  # Se elige el elemento más a la derecha como pivote
  pivote = array[alto]
  # Puntero para elementos mayores
  i = bajo - 1
  # Recorrer todos los elementos
  # Comparar cada elemento con el pivote
  for j in range(bajo, alto):
    if array[j] <= pivote:
      # Si se encuentra un elemento menor que el pivote
      # intercambiarlo con el elemento mayor señalado por i
      i = i + 1
      # Intercambiar el elemento en i con el elemento en j
      (array[i], array[j]) = (array[j], array[i])
  # Intercambiar el elemento del pivote con el elemento mayor especificado por i
  (array[i + 1], array[alto]) = (array[alto], array[i + 1])
  # Devolver la posición desde donde se realiza la partición
  return i + 1
# Función para realizar el ordenamiento rápido
def quickSort(array, bajo, alto):
  if bajo < alto:
    # Encontrar el elemento pivote de manera que los elementos menores que el pivote estén a la izquierda y los elementos mayores que el pivote estén a la derecha
    pi = particion(array, bajo, alto)
    # Llamada recursiva a la izquierda del pivote
    quickSort(array, bajo, pi - 1)
    # Llamada recursiva a la derecha del pivote
    quickSort(array, pi + 1, alto)

# Arreglo de 10 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10).tolist()
print("Arreglo no ordenado")
print(arr)

start_time = time.time()
tamaño = len(arr)
quickSort(arr, 0, tamaño - 1)
end_time = time.time()

print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 50 elementos con valores aleatorios
arr = np.random.randint(0, 100, 50).tolist()
print("Arreglo no ordenado")
print(arr)

start_time = time.time()
tamaño = len(arr)
quickSort(arr, 0, tamaño - 1)
end_time = time.time()

print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 100 elementos con valores aleatorios
arr = np.random.randint(0, 100, 100).tolist()
print("Arreglo no ordenado")
print(arr)

start_time = time.time()
tamaño = len(arr)
quickSort(arr, 0, tamaño - 1)
end_time = time.time()

print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 500 elementos con valores aleatorios
arr = np.random.randint(0, 100, 500).tolist()
print("Arreglo no ordenado")
print(arr)

start_time = time.time()
tamaño = len(arr)
quickSort(arr, 0, tamaño - 1)
end_time = time.time()

print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 1000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 1000).tolist()
print("Arreglo no ordenado")
print(arr)

start_time = time.time()
tamaño = len(arr)
quickSort(arr, 0, tamaño - 1)
end_time = time.time()

print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 2000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 2000).tolist()
print("Arreglo no ordenado")
print(arr)

start_time = time.time()
tamaño = len(arr)
quickSort(arr, 0, tamaño - 1)
end_time = time.time()

print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 5000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 5000).tolist()
print("Arreglo no ordenado")

start_time = time.time()
tamaño = len(arr)
quickSort(arr, 0, tamaño - 1)
end_time = time.time()

print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")

# Arreglo de 10000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10000).tolist()
print("Arreglo no ordenado")
print(arr)

start_time = time.time()
tamaño = len(arr)
quickSort(arr, 0, tamaño - 1)
end_time = time.time()

print('Arreglo ordenado en orden ascendente:')
print(arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")


