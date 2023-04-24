import numpy as np


def read_sparse_matrix(file_path):
    """
    Functie care citeste matricea dimensiunea si matricea rara din fisier si o stocheaza intr-un mod eficient ca un dictionar
    :param file_path:
    :return: n, A_dict
    """
    with open(file_path, 'r') as f:
        # citirea dimensiunii matricei
        n = int(f.readline().strip())

        if n < 1:
            raise ValueError("Dimensiunea matricei trebuie sa fie un numar pozitiv nenul.")

        # initializarea dictionarului pentru valorile nenule
        A_dict = {}

        # citirea valorilor nenule si a indicilor de linie si coloana corespunzatori
        for line in f:
            data = line.split(',')
            val = float(data[0])
            row = int(data[1]) - 1  # modificare: linia curenta se calculeaza de la 0, nu de la 1
            col = int(data[2]) - 1  # modificare: coloana curenta se calculeaza de la 0, nu de la 1

            if val == 0:
                raise ValueError("Elementele matricei trebuie sa fie numere pozitive nenule.")

            if row not in A_dict:
                A_dict[row] = {}
            A_dict[row][col] = val

        # construirea matricei rare folosind structura dictionarului
        return n, A_dict


def read_vector(file_path):
    """

    :param file_path:
    :return: b
    """
    # citirea vectorului termenilor liberi din fisier
    b = np.loadtxt(file_path, skiprows=1)
    return b


def gauss_seidel(A_dict, b, x0=None, max_iter=1000, tol=1e-6):
    """
    Functie care aplica metoda Gauss_Seidel pentru a calcula solutia pentru Ax=b

    :param A_dict:
    :param b:
    :param x0:
    :param max_iter:
    :param tol:
    :return: x, k+1(nr de iteratii)
    """
    n = len(A_dict)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy()
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            s = b[i]
            if i in A_dict:
                for j in A_dict[i]:
                    if j != i:
                        s -= A_dict[i][j] * x[j]
                x[i] = s / A_dict[i][i]
        if np.linalg.norm(x - x_old) < tol:
            break
    return x, k + 1


for i in range(1, 6):
    # citirea matricei rare din fisierul a_i.txt
    n, A_data = read_sparse_matrix(f"a_{i}.txt")
    # construirea matricei A din structura dictionarului
    A_dict = {}
    for row, data in A_data.items():
        for col, val in data.items():
            if row not in A_dict:
                A_dict[row] = {}
            A_dict[row][col] = val

    # citirea vectorului termenilor liberi din fisierul b_i.txt
    b = read_vector(f"b_{i}.txt")


    print(f"Vectorul termenilor liberi pentru sistemul {i}:")
    print(b)

    # rezolvarea sistemului Ax=b prin metoda Gauss-Seidel
    x_gs, num_iter = gauss_seidel(A_dict, b)

    # afisarea solutiei si a numarului de iteratii
    print(f"Solutia sistemului {i}:\n{x_gs}")
    print(f"Numarul de iteratii: {num_iter}")

    # calcularea normei ||AxGS - b||∞
    norm_diff = 0
    for row, data in A_dict.items():
        s = 0
        for col, val in data.items():
            s += val * x_gs[col]
        norm_diff = max(norm_diff, abs(s - b[row]))
    print(f"Norma diferenței: {norm_diff}\n")
