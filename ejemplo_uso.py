from METODOS.lineal_methods import gauss_elimination
# para los metodos lineales 
A = [[9, 77], [3, 55]]
B= [11, 13]
x = gauss_elimination(A, B)
print("LA SOLUCION  A TU EJERCICIO ES :", x)

# para los metodos no lineales 

from METODOS.nonlineal_methods import biseccion
raiz = biseccion(lambda x: x**3 - x - 4, 1, 8, 1e-6)
print("LA RAIZ :", raiz)