import numpy as np
import time
def moda(vector):
    # Caso base: si el vector tiene un solo elemento, ese es la moda
    if len(vector) == 1:
        return [vector[0]]

    # Dividir el vector en dos partes
    mitad = len(vector) // 2
    mitad_izquierda = vector[:mitad]
    mitad_derecha = vector[mitad:]

    # Encontrar las modas de ambas mitades de forma recursiva
    moda_izquierda = moda(mitad_izquierda)
    moda_derecha = moda(mitad_derecha)

    # Combinar las modas de ambas mitades
    modas_combinadas = moda_izquierda + moda_derecha

    # Contar la frecuencia de cada elemento en las modas combinadas
    frecuencia = {}
    for elemento in modas_combinadas:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1

    # Encontrar los elementos con la frecuencia máxima (modas)
    frecuencia_maxima = max(frecuencia.values())
    modas = [elemento for elemento, frec in frecuencia.items() if frec == frecuencia_maxima]

    return modas

# Arreglo de 10 elementos con valores aleatorios
arr = np.random.randint(0, 10, 10).tolist()
print(arr)
start_time = time.time()
resultado = moda(arr)
end_time = time.time()
print("Moda(s):", resultado)
print("Tiempo de ejecución para 10 elementos:", end_time - start_time, "segundos")

# Arreglo de 100 elementos con valores aleatorios
arr = np.random.randint(0, 100, 100).tolist()
start_time = time.time()
resultado = moda(arr)
end_time = time.time()
print("Moda(s):", resultado)
print("Tiempo de ejecución para 100 elementos:", end_time - start_time, "segundos")

# Arreglo de 1000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 1000).tolist()
start_time = time.time()
resultado = moda(arr)
end_time = time.time()
print("Moda(s):", resultado)
print("Tiempo de ejecución para 1000 elementos:", end_time - start_time, "segundos")

# Arreglo de 10000 elementos con valores aleatorios
arr = np.random.randint(0, 100, 10000).tolist()
start_time = time.time()
resultado = moda(arr)
end_time = time.time()
print("Moda(s):", resultado)
print("Tiempo de ejecución para 10000 elementos:", end_time - start_time, "segundos")

