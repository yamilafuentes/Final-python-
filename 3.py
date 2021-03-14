# Programar una funcion ProcesaMatriz que reciba una matriz y que forme y retorne un vector con la misma cantidad de elementos como
# columnnas tenga la matriz y con los valores de la cantidad de elementos negativos que tenga la columna correspondiente.

def procesa_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    vector = []

    for c in range(columnas):
        contador_negativos = 0
        for f in range(filas):
            if matriz[f][c] < 0:
                contador_negativos += 1
        vector.append(contador_negativos)

    return vector



matriz = [[-2,-1,5,6], [5,3,-2,-1], [-1,6,-7,9]]


print(procesa_matriz(matriz))





