import numpy as np
import random
def read_a(file):
    f = open(file, "r")
    text = f.read()
    ec = text.split("\n")

    l2=[]

    n = int(ec[0])

    for i in range(1, len(ec)):
        ec[i] = ec[i].replace(' ', '')
        l = ec[i].split(',')
        l2.append((float(l[0]), int(l[1]), int(l[2])))

    l2.sort(key = lambda x: x[1])

    # initializam matricea A cu zero-uri
    A = np.zeros((n, n))

    for val, row, col in l2:
        # adaugam valoarea la pozitia corespunzatoare in matricea A
        A[row, col] = val

    return A, l2

def generate_sparse_symmetric_matrix(n):
    A = [[0 for i in range(n)] for j in range(n)]
    indices = []
    values = []

    # generate k random indices and values
    k = random.randint(n, n*(n-1)//2)
    for i in range(k):
        row = random.randint(0, n-1)
        col_range = range(row + 1, n)
        if col_range:
            col = random.choice(col_range)
        else:
            col = row
        indices.append((row, col))
        value = random.uniform(0.1, 1.0)
        values.append(value)
        A[row][col] = value
        A[col][row] = value

    # assign values on diagonal
    for i in range(n):
        if A[i][i] == 0:
            value = random.uniform(0.1, 1.0)
            values.append(value)
            A[i][i] = value

    # create lists for each row
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            if A[i][j] != 0:
                row.append((j, A[i][j]))
        rows.append(row)

    return A, rows, values

def power_method(A, eps):
    A = np.array(A)  # convertim lista in ndarray
    n = np.array(A).shape[0]
    x = np.random.rand(n)
    x /= np.linalg.norm(x)
    while True:
        y = A.dot(x)
        lambda_max = y.max()
        y /= lambda_max
        if np.linalg.norm(x-y) < eps:
            break
        x = y
    return lambda_max, y

def is_symmetric(A):
    A = np.array(A)  # convertim lista in ndarray
    return np.allclose(A, A.T)

def SVD(A):
    A = np.array(A)
    U, s, Vt = np.linalg.svd(A)
    rang = np.linalg.matrix_rank(A)
    nr_cond = np.linalg.cond(A)

    return s, rang,nr_cond

def calculate_x_I(A, b, I):
    x_I = np.linalg.matrix_power(A, I).dot(b)
    x = np.linalg.solve(A, b)
    norm = np.linalg.norm(b - A.dot(x))
    return x_I, x, norm

A, l2a = read_a("m_rar_sim_2023_512.txt")
print(A)
print(l2a)
B, l2b = read_a("m_rar_sim_2023_1024.txt")
print(B)
print(l2b)
C, l2c = read_a("m_rar_sim_2023_2023.txt")
print(C)
print(l2c)
D, rows, values = generate_sparse_symmetric_matrix(512)
print(D)
print(rows)
print(values)

# Verificarea simetriei matricelor citite
print("A is symmetric:", is_symmetric(A))
print("B is symmetric:", is_symmetric(B))
print("C is symmetric:", is_symmetric(C))
print("D is symmetric:", is_symmetric(D))

# Calculul valorilor proprii de modul maxim și a vectorilor proprii asociați pentru matrici
lambda_max_A, v_A = power_method(A, 1e-6)
lambda_max_B, v_B = power_method(B, 1e-6)
lambda_max_C, v_C = power_method(C, 1e-6)
lambda_max_D, v_D = power_method(D, 1e-6)

print(lambda_max_A,"\n",v_A)
print(lambda_max_B,"\n",v_B)
print(lambda_max_C,"\n",v_C)
print(lambda_max_D,"\n",v_D)

print("A: ", SVD(A))
print("Pseudoinversa A:",np.linalg.pinv(A))
print("B: ", SVD(B))
print("Pseudoinversa B:",np.linalg.pinv(B))
print("C: ", SVD(C))
print("Pseudoinversa C:",np.linalg.pinv(C))
print("D: ", SVD(D))
print("Pseudoinversa D:",np.linalg.pinv(D))

b = np.random.rand(A.shape[1])
I = 2
x_I, x, norm = calculate_x_I(A, b, I)
print("x^I =", x_I)
print("Solutia sistemului Ax = b:", x)
print("Norma ||b - Ax||2:", norm)

b = np.random.rand(B.shape[1])
x_I, x, norm = calculate_x_I(B, b, I)
print("x^I =", x_I)
print("Solutia sistemului Bx = b:", x)
print("Norma ||b - Bx||2:", norm)

b = np.random.rand(C.shape[1])
x_I, x, norm = calculate_x_I(C, b, I)
print("x^I =", x_I)
print("Solutia sistemului Cx = b:", x)
print("Norma ||b - Cx||2:", norm)

D = np.array(D)
b = np.random.rand(D.shape[1])
x_I, x, norm = calculate_x_I(D, b, I)
print("x^I =", x_I)
print("Solutia sistemului Dx = b:", x)
print("Norma ||b - Dx||2:", norm)