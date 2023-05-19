def F(x):
    return x**3 - 2*x - 5

# Metoda de aproximare a derivatei folosind metoda centrului divizat
def approx_deriv(F, x, h=0.01):
    return (F(x+h) - F(x-h)) / (2*h)

# Definirea punctelor de început pentru metoda secantei
x0 = 1
x1 = 2

# Precizia dorită
sig = 0.0001

# Numărul maxim de iterații
max_iter = 1000

# Aproximarea derivatelor inițiale folosind metoda centrului divizat
fp0 = approx_deriv(F, x0)
fp1 = approx_deriv(F, x1)

# Itreații metodei secantei
for i in range(max_iter):
    x2 = x1 - F(x1) * (x1 - x0) / (F(x1) - F(x0))

    # Verificarea condiției de oprire
    if abs(x2 - x1) < sig:
        break

    # Actualizarea valorilor pentru următoarea iterație
    x0 = x1
    x1 = x2
    fp0 = fp1
    fp1 = approx_deriv(F, x1)

# Verificarea semnului celei de-a doua derivate în punctul găsit
fpp = approx_deriv(lambda x: approx_deriv(F, x), x2)
if fpp > 0:
    print("Solutia gasita este un punct de minim: x = ", x2)
else:
    print("Solutia gasita nu este un punct de minim: x = ", x2)
