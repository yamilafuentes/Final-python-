# Programar una funcion ReduceMatriz que reciba una matriz y un numero decimal de control como arguemento y que genere y retorne 
# una nueva matriz independiente e igual a la matriz dato  sin incluir aquellas filas donde el promedio de sus elementos sea menor
# al numero de control recibido. 

def reduce_matriz(M, control):
    matriz = M
    nueva_matriz = []
    
    
    for c in matriz:
        sumar = 0 
        for f in c:
            sumar +=  f 
        promedio_columna = sumar / len(c)
        if promedio_columna > control:
            nueva_matriz.append(c)
    return nueva_matriz
        


M = [[8,34,2], [33,4,2], [3,2,1]]

control = 9 

print(reduce_matriz(M, control))





