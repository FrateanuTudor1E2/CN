import numpy as np


def ex1(n, A, s):
    """
    Function that calculates b vector from R^n

    :param n:
    :param A:
    :param s:
    :return b:

    """
    b = np.zeros(n)

    for j in range(0, n):
        for i in range(0, n):
            b[i] += np.dot(s[j], A[i][j])

    return b


def qr_householder(A):
    """
    QR decomposition for A using Householder algorithm

    :param A:
    :return Q.T,A :

    """
    m, n = A.shape
    Q = np.eye(m)

    for j in range(n):
        # Select the subvector to be zeroed below the diagonal
        x = A[j:m, j]

        # Compute the Householder reflection vector
        v = np.zeros_like(x)
        v[0] = np.sign(x[0]) * np.linalg.norm(x)
        v = v + x
        v = v / np.linalg.norm(v)

        # Apply the Householder reflection to A and Q
        A[j:m, j:n] = A[j:m, j:n] - 2 * np.outer(v, np.dot(v, A[j:m, j:n]))
        Q[j:m, :] = Q[j:m, :] - 2 * np.outer(v, np.dot(v, Q[j:m, :]))

    return Q.T, A


from scipy.linalg import qr, solve_triangular


def solve_qr(A, b):
    """
    Funtion that solves A*x = b using a QR decomposition

    :param A:
    :param b:
    :return x:


    """
    Q, R = np.linalg.qr(A)
    x = solve_triangular(R, np.dot(Q.T, b))
    return x


def solve_householder(A, b):
    """
    Function that solves A*x = b by using a QR decomposition with the Housholder algoritm

    :param A:
    :param b:
    :return x:
    """
    Q, R = qr_householder(A)
    x = np.linalg.solve(R, np.dot(Q.T, b))
    return x


A = np.array([[1, 0, 2], [0, 1, 0], [0, 0, 1]])
s = np.array([1, 2, 3])
n = A.shape[0]

#ex1
b = ex1(3, A, s)
print(b, "\n")

#ex2
print(qr_householder(A), "\n")

#ex3
A = A + np.eye(n) * 1e-6
x_qr = solve_qr(A, b)
x_householder = solve_householder(A, b)
print(x_qr, "\n", x_householder)
norm_diff = np.linalg.norm(x_qr - x_householder, ord=2)
print("Norma diferenței între soluțiile xQR și xHouseholder:", norm_diff, "\n")

#ex4
error = np.linalg.norm(np.dot(A,x_householder) - b, ord=2)
print("4.1: ", error, '\n')
error = np.linalg.norm(np.dot(A,x_qr) - b, ord=2)
print("4.2: ", error, '\n')
norm_diff_xhs_s = np.linalg.norm(x_householder - s, ord=2)
norm_s = np.linalg.norm(s, ord=2)
error = norm_diff_xhs_s / norm_s
print("4.3: ", error, '\n')
norm_diff_xqr_s = np.linalg.norm(x_qr - s, ord=2)
error = norm_diff_xqr_s / norm_s
print("4.4: ", error, '\n')

#ex5
Q, R = qr_householder(A)
R_inv = np.linalg.inv(R)
A_inv_householder = np.dot (R_inv, Q.T)
A_inv_lib = np.linalg.inv(A)
norm_diff_inv = np.linalg.norm(A_inv_householder - A_inv_lib, ord=2)
print("5: ", norm_diff_inv)
