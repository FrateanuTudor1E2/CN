def ex1():
    u = 1
    while (u + 1 != 1):
        u /= 10

    return u


print("Ex1:\n", ex1(), "\n")

print("Ex2:")
print("pentru adunare:")

u = ex1()
x = 1.0
y = u
z = u

a = (x + y) + z
b = x + (y + z)

if a == b:
    print(True)
else:
    print(False)

print("pentru inmultire(x = 0.1):")

x = 0.1
y = u
z = u

a = (x * y) * z
b = x * (y * z)

if a == b:
    print(True, "\n")
else:
    print(False, "\n")

print("Ex3:")
