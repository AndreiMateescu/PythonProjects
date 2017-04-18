from functii import *

n = int(input("Dati dimensiune: "))
print(n)

matrice1 = creaza(n)
matrice2 = creaza(n)

print('1. Afisare \n2. Adunare \n3. Acces element \4. Cautare sir \n5. Inmultire \n6. Comparare')

aleg = int(input('Optiune: '))

while aleg != 0:
    if aleg == 1:
        print(matrice1)
        print(matrice2)
    if aleg == 2:
        matrice3 = adunare(matrice1,matrice2,n)
        print(matrice3)
    if aleg == 3:
        print('1. Prima matrice \n2. A doua matrice')
        aux = int(input('Aux: '))
        if aux == 1:
            x = get_value(matrice1,n)
        else:
            x = get_value(matrice2,n)
        print(x)
    if aleg == 4:
        sir = input('Sir: ')
        print('1. Prima matrice \n2. A doua matrice')
        aux = int(input('Aux: '))
        if aux == 1:
            cautare_sir(matrice1,n,sir)
        else:
            cautare_sir(matrice2,n,sir)
    if aleg == 5:
        matrice3 = transformare_matrice(matrice2,n)
        matrice4 = inmultire(matrice1,matrice3,n)

        print(matrice4)
    if aleg == 6:
        x = comparare(matrice1,matrice2,n)
        if x == 0:
            print('Egale')
        elif x == -1:
            print('1 < 2')
        else:
            print('1 > 2')
    aleg = int(input('Optiune: '))


