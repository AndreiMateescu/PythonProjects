def creaza(n):
    print('Creez matrice: ')
    matrice = []
    for j in range(n):
        for k in range(n):
            str = input()
            element = [j+1,k+1,str]
            matrice.append(element)
    return matrice

def acesare_element(matrice,linie,coloana):
    for element in matrice:
        if element[0] == linie and element[1] == coloana:
            return element[2]
            break

def get_value(matrice,n):
    linie = int(input('Dati linia: '))
    coloana = int(input('Dati coloana: '))
    for i in range(n):
        for j in range(n):
            return acesare_element(matrice,linie,coloana)

def cautare_sir(matrice,n,sir):
    ok = 0
    for i in range(n):
        for j in range(n):
            for element in matrice:
                if element[2] == sir:
                    ok = 1
    if ok == 1:
        print('Gasit')
    else:
        print('Nu s-a gasit')


def transformare_matrice(matrice,n):
    mat_nou = []

    for elem in matrice:
        elem_matrice_nou = []
        elem_matrice_nou.append(elem[0])
        elem_matrice_nou.append(elem[1])
        val = 0
        s = 1
        for k in range(len(elem[2])):
            val += (ord(elem[2][len(elem[2])-k-1])-ord('a'))*s;
            s *= 10
        elem_matrice_nou.append(val)
        mat_nou.append(elem_matrice_nou)

    return mat_nou

def adunare(matrice1,matrice2,n):
    noua_matrice =[]
    for i in range(n):
        for j in range(n):
            element_nou = []
            for element1 in matrice1:
                for element2 in matrice2:
                    if element1[0] == element2[0] == i+1 and element1[1] == element2[1] == j+1:
                        element = element1[2] + element2[2]
                        element_nou = [i+1,j+1,element]
                        noua_matrice.append(element_nou)
    return noua_matrice

def inmultire(matrice1,matrice2,n):
    matrice = []
    for i in range(n):
        for j in range(n):
            sum = ''
            for k in range(n):
                for element1 in matrice1:
                    for element2 in matrice2:
                        if element1[0] == i+1 and element1[1] == k+1 and element2[0] == k+1 and element2[1] == j+1:
                            sum = sum + element1[2]*element2[2]
            element_nou = [i+1,j+1,sum]
            matrice.append(element_nou)
    return matrice

def comparare(matrice1, matrice2, n):
    for i in range(n):
        for j in range(n):
            if matrice1[j][2] < matrice2[j][2]:
                return -1
            elif matrice1[j][2] > matrice2[j][2]:
                return 1
    return 0


