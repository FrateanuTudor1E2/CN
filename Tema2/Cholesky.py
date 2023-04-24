
import numpy as np
from scipy.linalg import lu_solve, lu_factor
import scipy
def matrice():
    """
    Creeaza matricea cu elemente date ca input de la tastatura

   returns:
        Matrice ca un array NumPy
    """
    Matrice = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, n):  # parcurgem doar partea superioara a matricei
            Matrice[i][j] = Matrice[j][i] = int(input(f"Introduceti elementul de pe pozitia ({i + 1},{j + 1}): "))

    return np.array(Matrice)


def cholesky(A):
    """
    Algoritm de descompunere LDL^T (Cholesky) pentru matrice simetrică pozitiv definită.

    Acest algoritm calculează o descompunere LDL^T a matricei A, unde L este o matrice inferior
    triunghiulară cu toate elementele de pe diagonala principală egale cu 1 și D este o matrice diagonala.

    Args:
        A: matricea simetrică pozitiv definită pentru care se calculează descompunerea Cholesky

    Returns:
        L, D: matricea L și matricea D, reprezentând descompunerea LDL^T a matricei A
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    D = np.zeros((n, n))

    for j in range(n):
        L[j, j] = 1
        for k in range(j):
            sum1 = sum(L[j, m] * D[m, m] * L[k, m] for m in range(k))
            L[j, k] = (A[j, k] - sum1) / (D[k, k])
        sum2 = sum(L[j, m] ** 2 * D[m, m] for m in range(j))
        D[j, j] = A[j, j] - sum2

    return L, D


def determinant_cholesky(A):
    """
    Calculează determinantul unei matrice simetrice pozitiv definite folosind descompunerea Cholesky.

    Args:
        A: matricea simetrică pozitiv definită pentru care se calculează determinantul

    Returns:
        det_A: determinantul matricei A
    """
    n = A.shape[0]
    L, D = cholesky(A)

    # Calculăm determinantul matricei D
    det_D = 1
    for i in range(n):
        det_D *= D[i, i]

    # Calculăm determinantul matricei L transpusa
    det_Lt = 1
    for i in range(n):
        det_Lt *= L[i, i]

    # Calculăm determinantul matricei A
    det_A = det_D * (det_Lt ** 2)

    return det_A


def solve_cholesky(A, b):
    """
    Calculeaza solutia aproximativa a sistemului Ax = b folosind descompunerea Cholesky.

    Args:
        A: matricea sistemului
        b: vectorul termenilor liberi

    Returns:
        xChol: solutia aproximativa a sistemului Ax = b
    """
    L, D = cholesky(A)

    # rezolvam sistemul Ly = b prin substitutie directa
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, j] * y[j] for j in range(i))) / L[i, i]

    # rezolvam sistemul L^Tx = y prin substitutie inversa
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(L[j, i] * x[j] for j in range(i + 1, n))) / L[i, i]

    # returnam solutia aproximativa xChol
    return x


n = int(input("Introduceti dimensiunea matricei A: "))
b = np.random.rand(n)
A = matrice()

print("LDL^T:\n", cholesky(A), "\n")
print("Det(A):\n", determinant_cholesky(A), "\n")
print("Solutia aproximativa xChol:\n ", solve_cholesky(A, b))
print("\n######################################################\n")
# Redefinim matricea A si vectorul b
A = np.array([[1, 2, 3], [2, 8, 4], [3, 4, 11]])
b = np.array([1, 2, 3])

# Recalculam descompunerea LU a matricei A
lu, piv = lu_factor(A)

# Afisam matricele P, L si U
P,L,U = scipy.linalg.lu(A)
print("Matricea P:")
print(P)
print("Matricea L:")
print(L)
print("Matricea U:")
print(U)

# Rezolvam sistemul Ax = b
x = lu_solve((lu, piv), b)

# Afisam solutia x
print("Solutia sistemului Ax = b:")
print(x,"\n")
# calculam Ax cu solutia x obtinuta cu Cholesky
Ax = np.dot(A, x)

# calculam norma diferentei Ax - b
norm = np.linalg.norm(Ax - b)

print(f"Norma euclidiana a diferentei dintre Ax si b este: {norm}")