import numpy as np

# =====================================================================
# 1. PRODUCTO PUNTO (Entre dos vectores de 1D)
# =====================================================================
# El producto punto toma dos vectores del mismo tamaño, multiplica sus 
# elementos correspondientes uno a uno y los suma, devolviendo un escalar.

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# Opción A: Usando np.dot()
producto_punto_op1 = np.dot(vector_a, vector_b)

# Opción B: Usando el operador @ (introducido en Python 3.5+)
producto_punto_op2 = vector_a @ vector_b

print("--- PRODUCTO PUNTO ---")
print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}")
print(f"Resultado (opción 1): {producto_punto_op1}")
print(f"Resultado (opción 2): {producto_punto_op2}\n")


# =====================================================================
# 2. MULTIPLICACIÓN DE MATRICES (2D)
# =====================================================================
# Recuerda que para multiplicar una matriz A (m x n) por una matriz B (n x p),
# el número de columnas de A debe ser igual al número de filas de B.

# Matriz de 2x3
matriz_A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Matriz de 3x2
matriz_B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

# Opción A: Usando np.matmul() (la función recomendada para matrices)
producto_matriz_op1 = np.matmul(matriz_A, matriz_B)

# Opción B: Usando el operador @
producto_matriz_op2 = matriz_A @ matriz_B

# Opción C: Usando np.dot() (también funciona para 2D, pero matmul es preferible)
producto_matriz_op3 = np.dot(matriz_A, matriz_B)

print("--- MULTIPLICACIÓN DE MATRICES ---")
print("Matriz A (2x3):\n", matriz_A)
print("Matriz B (3x2):\n", matriz_B)
print("\nResultado Matriz (2x2) usando matmul():\n", producto_matriz_op1)
print("\nResultado Matriz (2x2) usando operador @:\n", producto_matriz_op2)
