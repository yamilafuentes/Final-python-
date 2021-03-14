# Programar una funcion leematriz(minimo,maximo) que cargue en memoria y devuelva una matriz de numeros enteros que ingresa el operador.
# La funcion recibe por parametro un valor minimo y un valor maximo aceptable. Los valores validos seran aquellos que sean mayores 
# o iguales al minimo aceptable y menores o igual al maximo aceptable y que ademas sean numeros impares. Al inicio de la funcion se 
# debera solicitar al operador que ingrese la cantidad de filas y columnas que que tendra la matriz a cargar.
# La funcion debera pedir cada elemento por fila y controlar que el valor sea valido, en caso contrario debera solicitar el ingreso 
# nuevamente del elemento de la matriz hasta que se ingrese uno valido.


def lee_matriz(minimo, maximo):
    valor_minimo = minimo
    valor_maximo = maximo
    matriz = []
    filas = int(input("Cantidad de filas: "))
    columnas = int(input("Cantidad de columnas: "))

    for i in range(filas):
        matriz.append([0] * columnas)

    for c in range(columnas):
        for f in range(filas):
            while True:            
                numero = int(input("Elemento %d, %d : " % (c,f)))
                if numero >= valor_minimo and numero <= valor_maximo:
                    if numero % 2 != 0:
                        matriz[c][f] = numero
                        break 
    return matriz
                      


minimo = 2
maximo = 10                        

print(lee_matriz(minimo,maximo))

            
