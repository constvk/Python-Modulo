import os

def sum(x, y):
    return x % y

print("Módulo de dois números")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

print ("")
print ("O resultado da Módulo é %d" %sum(x, y))

os.system("pause")
