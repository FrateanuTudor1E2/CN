import random

def generate_sparse_symmetric_matrix_dict(n, p):
    """
    Functia genereaza o matrice rara si simetrica sub forma de dictionar, cu dimensiunile n x n si p elemente nenule
    """
    # initializam dictionarul
    matrix_dict = {}
    # generam p elemente nenule si le punem in dictionar
    for _ in range(p):
        # generam o pozitie aleatorie in jumatatea triunghiulara superioara
        i = random.randint(0, n-1)
        j = random.randint(i, n-1)
        # generam valoarea pentru aceasta pozitie
        val = random.randint(1, 10)
        # punem valoarea in dictionar pe pozitia (i,j)
        if i not in matrix_dict:
            matrix_dict[i] = {}
        matrix_dict[i][j] = val
    # completam si jumatatea triunghiulara inferioara
    for i in range(n):
        for j in range(i):
            if j in matrix_dict and i in matrix_dict[j]:
                # elementul a fost deja generat si pus in dictionar
                continue
            elif i in matrix_dict and j in matrix_dict[i]:
                # elementul a fost deja generat si pus in dictionar
                continue
            else:
                # generam o valoare aleatoare si o punem in dictionar pe pozitia (i,j) si (j,i)
                val = random.randint(1, 10)
                if i not in matrix_dict:
                    matrix_dict[i] = {}
                if j not in matrix_dict:
                    matrix_dict[j] = {}
                matrix_dict[i][j] = val
                matrix_dict[j][i] = val
    return matrix_dict

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





n=600
p = n
A_rand = generate_sparse_symmetric_matrix_dict(n, p)
#print(A_rand)

# citirea matricilor rare din fisierele date
n1, A1 = read_sparse_matrix(f"m_rar_sim_2023_512.txt")
n2, A2 = read_sparse_matrix(f"m_rar_sim_2023_1024.txt")
n3, A3 = read_sparse_matrix(f"m_rar_sim_2023_2023.txt")
