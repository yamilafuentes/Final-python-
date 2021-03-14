# Programar una funcion ReduceMatriz que reciba una matriz y un numero decimal de control como arguemento y que genere y retorne 
# una nueva matriz independiente e igual a la matriz dato sin incluir aquellas filas donde el promedio de sus elementos sea menor
# al numero de control recibido.

def reduce_matriz(m, control):
    matriz = m
    columnas = len(matriz)
    filas = len(matriz[0])
    nueva_matriz = []
    
    

    print(matriz)  

    for f in range(filas):
        suma_filas = 0
        cantidad_elementos = 0
        filasNuevaMatriz = []

        for c in range(columnas):
            print("c: " + str(c) + " f: " + str(f))                               
            print("valor: " + str(matriz[c][f]))
            suma_filas += matriz[c][f] 
            cantidad_elementos += 1
            filasNuevaMatriz.append(matriz[c][f])
            print(filasNuevaMatriz)

        promedio_fila = suma_filas / cantidad_elementos
        if promedio_fila > control:
            nueva_matriz.append(filasNuevaMatriz)

    for f in len(nueva_matriz):
        if f < 



            

m = [[8,34,2], [33,4,2], [3,2,1]]
control = 9.

print(reduce_matriz(m, control))



