# Prpgramar una funcion MuestraMatriz que reciba por parmetro una matriz de numero enteros y la debe mostrar en pantalla siguiendo
# el formato que se muestra en el ejemplo 
"""
   ---------------
   !  45  !  56  !
   ***************
   !  120 !  5   !
   ***************
   ! -45  !  8   !
   ---------------
"""


def muestra_matriz(matriz): 
    cant_filas = len(matriz)
    cant_columnas = len(matriz[0])
   
    for f in range(cant_filas):
        for c in range(cant_columnas):
            print(matriz[f][c])
    return

   


matriz = [[1,2,3], [4,5,6]]

print(muestra_matriz(matriz))

