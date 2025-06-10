"""
Crea una funcion que reciba por parámetro dos matrices y retorne una matriz que sea producto de
las dos anteriores recibidas por parametro

Para multiplicar matrices, es crucial que el número de columnas de la primera matriz sea igual 
al número de filas de la segunda matriz. La matriz resultante tendrá el mismo número de filas 
que la primera matriz y el mismo número de columnas que la segunda matriz. La multiplicación se 
realiza multiplicando cada fila de la primera matriz por cada columna de la segunda matriz 
y sumando los productos. 

Detalles:
1. Condición de Compatibilidad:
Para que la multiplicación de dos matrices A y B esté definida, 
el número de columnas de A debe ser igual al número de filas de B. 
Si A es de tamaño m x n y B es de tamaño n x p, entonces el producto AB estará definido y será de tamaño m x p. 
 
2. Procedimiento de Multiplicación:
Se elige una fila de la primera matriz (A) y una columna de la segunda matriz (B).
Se multiplican los elementos de la fila por los elementos de la columna, y se suman los productos. 
Este proceso se repite para todas las filas de la primera matriz y todas las columnas de la segunda matriz. 
"""