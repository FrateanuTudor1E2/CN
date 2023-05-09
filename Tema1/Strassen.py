def multiply_Strassen(A, B, n, n_min):
    """

    :param A:
    :param B:
    :param n or q:
    :param n_min or d:
    :return: AxB
    """
    if n <= n_min:
        # If the size of the matrices is small enough, use regular matrix multiplication
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    else:
        # Split the matrices into submatrices
        m = n // 2
        A11, A12, A21, A22 = A[:m], A[:m], A[m:], A[m:]
        B11, B12, B21, B22 = B[:m], B[:m], B[m:], B[m:]

        # Compute the seven products
        P1 = multiply_Strassen(A11, subtract(B12, B22), m, n_min)
        P2 = multiply_Strassen(add(A11, A12), B22, m, n_min)
        P3 = multiply_Strassen(add(A21, A22), B11, m, n_min)
        P4 = multiply_Strassen(A22, subtract(B21, B11), m, n_min)
        P5 = multiply_Strassen(add(A11, A22), add(B11, B22), m, n_min)
        P6 = multiply_Strassen(subtract(A12, A22), add(B21, B22), m, n_min)
        P7 = multiply_Strassen(subtract(A11, A21), add(B11, B12), m, n_min)

        # Compute the four quadrants of the product matrix
        C11 = subtract(add(add(P5, P4), P6), P2)
        C12 = add(P1, P2)
        C21 = add(P3, P4)
        C22 = subtract(add(add(P5, P1), P3), P7)

        # Combine the four quadrants into a single matrix
        C = [[0] * n for i in range(n)]
        for i in range(m):
            for j in range(m):
                C[i][j] = C11[i][j]
                C[i][j + m] = C12[i][j]
                C[i + m][j] = C21[i][j]
                C[i + m][j + m] = C22[i][j]

        return C


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

A = [[1, 2, 3, 4], [3, 4, 5 ,6], [5, 6, 7, 8],[7, 8, 9, 10]]
B = [[5, 6, 7, 8], [7, 8, 9, 10], [9, 10, 11, 12],[11, 12, 13, 14]]
n = 4
n_min = 1
C = multiply_Strassen(A,B,n,n_min)
print(C)
