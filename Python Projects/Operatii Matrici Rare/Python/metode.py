#metoda creare matrice
#are ca parametrii liniile si coloanele, trebuie sa tastez numarul de elemente nenule
#cele 3 cicluri while: intra in unul din ele daca indicele liniei sau / si coloanei > numarul de linii, coloane
def create(lines,columns):
    matrice = [] #definesc o lista cu numele matrice

    n = int(input("Enter the number of elements: ")) #numarul de elemente diferite de 0 din lista
    print(n)

    for i in range(n):
        str = input() #citesc secventa: linie,coloana,valoare ca un sir
        tokens = str.split(' ') #despart sirul astfel incat sa pot sa introduc elementele (ca numere)
        element = [int(tokens[0]), int(tokens[1]), float(tokens[2])]


        #de fiecare data cand introduc o valoare peste numarul de coloane si linii
        #imi cere sa ii dau un numar corect de linie si/sau coloana
        while int(tokens[0]) > lines:
            tokens[0] = int(input('Enter the line again (line > no of lines): '))

        element = [int(tokens[0]), int(tokens[1]), float(tokens[2])] # updatez elementul

        while int(tokens[1]) > columns:
            tokens[1] = int(input('Enter the columns again (column > no of columns): '))

        element = [int(tokens[0]), int(tokens[1]), float(tokens[2])]

        while int(tokens[0]) > lines and int(tokens[1]) > columns:
            tokens[0] = int(input('Enter the line again (line > no of lines): '))
            tokens[1] = int(input('Enter the columns again (column > no of columns): '))

        element = [int(tokens[0]), int(tokens[1]), float(tokens[2])]

        matrice.append(element) #adaug elementul la sfarsitul ultimului element din lista

    return matrice

#creez o matrice unitate: 1 pe diagonala principala
def create_unit(lines):
    matrice = [] #definesc o lista cu numele matrice

    n = lines #numarul de elemente este egal cu numar de linii: Exemplu: 3 linii, deci voi avea 3 de 1 pe diag principala

    for i in range(n):
        tokens = [i+1,i+1,1] #tip lista care retine linia,coloana si valoarea 1, atunci cand linia = coloana
        matrice.append(tokens) #adaug elementul la sfarsitul ultimului element din lista

    return matrice

#metoda care returneaza transpusa
def trans_matrice(matrix_one,lines,columns):
    matrice = [] #definesc o lista cu numele matrice

    lines2 = columns #coloanele devin linii
    columns2 = lines #liniile devin coloane

    for i in range(lines): #parcurgere i=1,lines
        for j in range(columns):
            for element in matrix_one:
                # verific daca elementul se poate aseza la fel in matrice (linia si coloana ii corespund ca inainte)
                if i == element[0] and j == element[1]:
                    new_element = [element[0],element[1],element[2]] #un nou element de tip lista
                    matrice.append(new_element) #il adaug
                else:
                    # pozitiile nu mai coincid si trebuie inversate pentru a fi corecta transpusa
                    new_element = [element[1],element[0],element[2]]
                    matrice.append(new_element)
    return matrice


#verific daca exista un element (daca linia si coloana exista, atunci el este nenul).
# Ma folosesc de aceasta metoda la afisare. Afisez elementul sau 0 in caz ca nu exista (conform unei matrici rare)
def exists(matrice,line,column):
    for element in matrice:
        if element[0] == line and element[1] == column:
            return element[2]
    return 0

#afisez lista ca o matrice
def print_matrice(matrice,lines,columns):
    for i in range(lines):
        for j in range(columns):
            x = exists(matrice,i+1,j+1)
            print(x, end=" ")#specific sa nu treaca la linia urmatoare, ci endul sa fie spatiu
        print('\n')
    print('\n')


#gasesc pozitia pentru adunare/scadere.
def find_pos(matrice, line, col):
	for i in range(len(matrice)):
		if matrice[i][0] == line and matrice[i][1] == col:
			return i
	return -1 #daca nu a gasit returneaza -1, care este diferit de 0..sa stiu in ce caz ma aflu

#metoda de adunare a 2 matrici (au acelasi numar de linii si de coloane)
#Adun elementele daca ambele exista
#daca din prima matrice exista si in a 2-a nu exista atunci elementul = elementul din prima matrice
#daca in prima matrice nu am si am element in a 2-a matrice, elementul = elementul din a 2-a matrice
def addition(matrix_one,matrix_two,lines,columns):
	result = [] #rezultatul de tip lista
	for i in range(lines):
		for j in range(columns): #parcurgere
			pos_one = find_pos(matrix_one, i + 1, j + 1) #pozitiile
			pos_two = find_pos(matrix_two, i + 1, j + 1)
            # daca cel putin una este nenula, se continua. Nu are rost pentru ambele nule, rezultatul va fi 0
			if pos_one != -1 or pos_two != -1:
				element = [i + 1, j + 1, 0] #momentan valoarea = 0

                # cazurile despre care am vorbit
				if pos_one != -1:
					element[2] += matrix_one[pos_one][2]

				if pos_two != -1:
					element[2] += matrix_two[pos_two][2]

				result.append(element)

	return result

#metoda diference este similara adunarii
def diference(matrix_one,matrix_two,lines,columns):
    result = []
    for i in range(lines):
        for j in range(columns):
            pos_one = find_pos(matrix_one,i+1,j+1)
            pos_two = find_pos(matrix_two,i+1,j+1)

            if pos_one != -1 or pos_two != -1:
                element = [i+1,j+1,0]

                if pos_one != -1:
                    if pos_two != -1:
                        element[2] = element[2] + matrix_one[pos_one][2] - matrix_two[pos_two][2]
                if pos_one != -1:
                    element[2] = matrix_one[pos_one][2]
                if pos_two != -1:
                    element[2] = element[2] - matrix_two[pos_two][2]

                result.append(element)

    return result

#prin aceasta metoda verific daca un element exista in matrice sau nu. Daca rezultatul este != 0 atunci exista
def find_element_value(matrice,line,column,value):
    for element in matrice:
         if element[0] == line and element[1] == column and element[2] == value:
               return value
    return 0

#Vreau sa aflu daca un numar tastat de la tastatura se gaseste in matrice
def acces_elements_value(matrice,lines,columns):
    aux = float(input('Enter the element witch you want to find: '))

    ok = False #presupun ca nu gasesc elementul
    for i in range(lines):
        for j in range(columns):
            x = find_element_value(matrice,i+1,j+1,aux) #returneaza 0 sau elementul (metoda de mai sus)
            if x != 0:
                ok = True #deci exista, atunci memorez pozitiile si valoarea, pentru a le afisa
                value = x
                line = i+1
                column = j+1
    if ok == True:
        print('Found ', value, 'at line ', line, 'and column ', column )
    else:
        print('Didn\'t find') #in caz contrat afiseaza ca nu-l gaseste

#imi returneaza valoarea elementului daca indicii exista, altfel 0 (imi foloseste la cautarea prin indici)
#Vreau sa aflu daca elementul exista cu linia x si coloana y exista
def find_element(matrice,line,column):
    for element in matrice:
        if element[0] == line and element[1] == column:
            return element[2]
    return 0

#daca indicele de linie si coloana exista memorat, atunci afisez elementul corespunsator, in caz contrar afisez ca nu-l gaseste
def acces_element(matrice):
    aux_line = int(input('Enter the line of element witch you want to find: '))
    aux_column = int(input('Enter the column of element witch you want to find: '))

    x = find_element(matrice, aux_line, aux_column)
    if x != 0:
        print('Element found: ', x)
    else:
        print('Not found')

#m-am folosit de aceasta metoda pentru a verifica daca introduce cum trebuie datele
def true_or_false(matrice,lines,columns):
    for i in range(lines):
        for j in range(columns):
            for element in matrice:
                print(element[0],element[1],element[2])

#inmultirea. Simulez inmultirea ca pe matrici normale
#Am ca parametrii liniile si coloanele primeia, si coloanele celei de-a 2-a. Nu am nevoie de liniile celei de-a 2-a (linii2 = coloane1)
def multiplication(matrix_one,matrix_two,lines1,columns1,columns2):
    matrice = []
    for i in range(lines1):
        for j in range(columns2):
            sum = 0.0
            for k in range(columns1):
                for element_one in matrix_one:
                    for element_two in matrix_two:
                        # daca eixsta elementele nenule
                        if element_one[0] == i+1 and element_one[1] == k+1 and element_two[0] == k+1 and element_two[1] == j+1:
                            sum = sum + element_one[2]*element_two[2] #suma elementelor inmultite de pe linie si coloana
            if sum != 0:# daca e diferita de 0 atunci adaug elementul in matricea rezultat
                new_element = [i+1, j+1, sum]
                matrice.append(new_element)

    return matrice

