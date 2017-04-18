from metode import *

n = int(input('Introduceti numarul: '))

print('1. Generarea partitiilor','\n2. Determinarea celui de-al n-lea palindrom','\n3. Afisarea numarului')
print('\n')
print('Optiune: ')
optiune = int(input('Dati optiunea: '))
while optiune != 0:
    if optiune == 1:
        partitii(n)
    if optiune == 2:
        x = palindrom(n)
        print(x)
    if optiune == 3:
        print(n)
    optiune = int(input('Dati optiunea: '))