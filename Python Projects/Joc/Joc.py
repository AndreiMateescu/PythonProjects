class Joc(object):

    def __init__(self):   #Constructorul clasei Joc

        self.matrice =  [[False] * (10) for lines in range(10)]   # o matrice de 10 pe 10 initializzata cu False reprezentand matricea jocului
        self.orizontal = 0  # o variabila in care se retine unde se afla linia orizontala
        self.principal()    # se apeleaza functia principal a clasei Joc

    def checkColt (self):  # Functia checkColt care verifica in care dintre cele 4 colturi se gaseste partea cu b
                           # Cele 4 colturi sunt dupa cum urmeaza :   1 2
                           #                                          3 4

        print("<1, 1>")    # interogheaza jucatorul x in priviinta coordonatelor 1 1
        raspuns = input()  # citeste raspunsul jucatorului x
        if raspuns == "b": # Daca raspunsul este b inseamna ca acel colt se afla in partea din stanga sus
            return 1       # Daca se afla in cotul de coordonate 1 1 se va returna 1
        print("<1, 10>")   # interogheaza jucatorul x in priviinta coordonatelor 1 1
        raspuns = input()  # citeste raspunsul jucatorului x
        if raspuns == "b": # Daca raspunsul este b inseamna ca acel colt se afla in partea din dreapta sus
            return 2       # Daca se afla in cotul de coordonate 1 10 se va returna 2
        print("<10, 1>")   # interogheaza jucatorul x in priviinta coordonatelor 1 1
        raspuns = input()  # citeste raspunsul jucatorului x
        if raspuns == "b": # Daca raspunsul este b inseamna ca acel colt se afla in partea din stanga jos
            return 3       # Daca se afla in cotul de coordonate 10 1 se va returna 3
        print("<10, 10>")  # interogheaza jucatorul x in priviinta coordonatelor 1 1
        raspuns = input()  # citeste raspunsul jucatorului x
        if raspuns == "b": # Daca raspunsul este b inseamna ca acel colt se afla in partea din dreapta jos
            return 4       # Daca se afla in cotul de coordonate 10 10 se va returna 4

    def principal(self):   # Functia principal este functia care in functie de zona unde se afla partea completata cu b
                           # apeleaza functile care sunt necesare pentru determinarea celor doua linii trasate
        aux = self.checkColt()  # aux este o variabila auxiliara care este egalata cu raspunsul returnat de checkColt
        if aux == 1:      # Daca aux este 1 inseamna ca coltul se afla in partea din dreapta jos
            self.colt1()  # Se apeleaza functia colt1 care va determina linia verticala si orizontala
            self.creereMat1()  # Se apeleaza functia creereMat1 care modifica matricea pentru cazul in care bucata din coltul 1 este b
        if aux == 2:      # Daca aux este 2 inseamna ca coltul se afla in partea din dreapta jos
            self.colt2()  # Se apeleaza functia colt2 care va determina linia verticala si orizontala
            self.creereMat2()  # Se apeleaza functia creereMat1 care modifica matricea pentru cazul in care bucata din coltul 2 este b
        if aux == 3:      # Daca aux este 3 inseamna ca coltul se afla in partea din dreapta jos
            self.colt3()  # Se apeleaza functia colt3 care va determina linia verticala si orizontala
            self.creereMat3()  # Se apeleaza functia creereMat1 care modifica matricea pentru cazul in care bucata din coltul 3 este b
        if aux == 4:      # Daca aux este 4 inseamna ca coltul se afla in partea din dreapta jos
            self.colt4()  # Se apeleaza functia colt4 care va determina linia verticala si orizontala
            self.creereMat4()  # Se apeleaza functia creereMat1 care modifica matricea pentru cazul in care bucata din coltul 4 este b

        self.print()   # Se apeleaza functia de printare a rezultatului ce consta in coordonatele intre care se afla cele doua linii
        self.printMat()  # Se apeleaza functia care printeazza matricea

    def print(self):    # Functia care printeaza rezultatul care consta in coordonatele intre care se afla cele doua linii
        print("Linia orizontala se afla intre :", self.orizontal, " si ",self.orizontal + 1)
        print("Linia verticala se afla intre :", self.vertical, " si ", self.vertical + 1)

    def creereMat1(self):  # Functia care modifica/completeaza matricea initializata cu False cu True unde se afla b , cand campurile
                           # b se afla in coldul din stanga sus al matricei
        for i, linie in enumerate(self.matrice):
            for j, element in enumerate(linie):
                if i < self.orizontal and j < self.vertical: # Daca i si j corespund conditilor se afla in coltul corespunzator
                    self.matrice[i][j] = True   # egaleaza campurile care corespund campurilor b cu True

    def creereMat2(self):  # Functia care modifica/completeaza matricea initializata cu False cu True unde se afla b , cand campurile
                           # b se afla in coldul din dreapta sus al matricei
        for i, linie in enumerate(self.matrice):
            for j, element in enumerate(linie):
                if i < self.orizontal and j >= self.vertical: # Daca i si j corespund conditilor se afla in coltul corespunzator
                    self.matrice[i][j] = True   # egaleaza campurile care corespund campurilor b cu True

    def creereMat3(self):  # Functia care modifica/completeaza matricea initializata cu False cu True unde se afla b , cand campurile
                           # b se afla in coldul din stanga jos al matricei
        for i, linie in enumerate(self.matrice):
            for j, element in enumerate(linie):
                if i >= self.orizontal and j < self.vertical: # Daca i si j corespund conditilor se afla in coltul corespunzator
                    self.matrice[i][j] = True   # egaleaza campurile care corespund campurilor b cu True

    def creereMat4(self):  # Functia care modifica/completeaza matricea initializata cu False cu True unde se afla b , cand campurile
                           # b se afla in coldul din dreapta jos al matricei
        for i, linie in enumerate(self.matrice):
            for j, element in enumerate(linie):
                if i >= self.orizontal and j >= self.vertical: # Daca i si j corespund conditilor se afla in coltul corespunzator
                    self.matrice[i][j] = True   # egaleaza campurile care corespund campurilor b cu True

    def printMat(self):    # Functia care printeaza matricea
        rezultat = ''      # rezultat este o variabila de tip strring in care se construieste matricea
        for i, linie in enumerate(self.matrice):
            for j, element in enumerate(linie):
                if self.matrice[i][j]:
                    rezultat += ' b'
                else:
                    rezultat += ' a'
            rezultat += '\n'  # rezultat += '\n' ca sa treaca pe linia urmatoare odata cu schimbarea linilor in forul cu i

        print(rezultat)  # priteaza matricea rezultat

    def colt1(self): # Functia colt1 care determina care sunt coordonatele linilor, cea verticala si orizontala in cazul in care
                     # zona b este in coltul 1 ( stanga sus )
        for i in range(9):
            print("<",i+2,", ",i+2,">")  # interogheaza jucatorul x in privinta coordonatelor de pe diagonala cu coltul 1
            raspuns = input()
            if raspuns == "a":  # La intalnirea primului a inseamna ca zona b a fost depasita si a fost gasita linia verticala
                self.vertical = i+1 # Linia verticala este egala cu pozitia anterioara a coloanei ( pe axa x )
                break
        for i in range(10-(self.vertical)):  # Stiind coordonata verticala este interogat jucatorul despre coodronatele de mai jos
            print("<", i + self.vertical + 1, ", ", self.vertical, ">")  # pentru a determina unde se afla cea orizontala
            raspuns = input()
            if raspuns == "a":  # La intalnirea primului a inseamna ca zona b a fost depasita si a fost gasita linia orizontala
                self.orizontal = i + self.vertical
                break


    def colt2(self):  # Functia colt1 care determina care sunt coordonatele linilor, cea verticala si orizontala in cazul in care
                      # zona b este in coltul 2 ( dreapta sus )
        for i in range(9):
            print("<", i+2, ", ", 9-i, ">")  # interogheaza jucatorul x in privinta coordonatelor de pe diagonala cu coltul 2
            raspuns = input()
            if raspuns == "a":  # La intalnirea primului a inseamna ca zona b a fost depasita si a fost gasita linia verticala
                self.vertical = 9 - i # Linia verticala este egala cu pozitia coloanei ( pe axa x )
                aux = i + 2  # Se foloseste un auxiliar pentru a retine coordonata unde se afla anterior linia (pe axa y )
                break
        for i in range(self.vertical): # Stiind coordonata verticala este interogat jucatorul despre coodronatele de mai jos
            print("<", i + aux , ", ", self.vertical + 1, ">")  # pentru a determina unde se afla cea orizontala
            raspuns = input()
            if raspuns == "a": # La intalnirea primului a inseamna ca zona b a fost depasita si a fost gasita linia orizontala
                self.orizontal = i + aux - 1
                break


    def colt3(self): # Functia colt1 care determina care sunt coordonatele linilor, cea verticala si orizontala in cazul in care
                     # zona b este in coltul 3 ( stanga jos )
        for i in range(9):
            print("<", 9-i, ", ", i+2, ">")  # interogheaza jucatorul x in privinta coordonatelor de pe diagonala cu coltul 3
            raspuns = input()
            if raspuns == "a":  # La intalnirea primului a inseamna ca zona b a fost depasita si a fost gasita linia orizontala
                self.orizontal = 9 - i   # Linia orizontala este egala cu pozitia liniei ( pe axa y )
                aux = i + 2  # Se foloseste un auxiliar pentru a retine coordonata unde se afla anterior coloana (pe axa x )
                break
        for i in range(10 - (aux - 1)):  # Stiind coordonata orizontala este interogat jucatorul despre coodronatele din dreapta
            print("<", self.orizontal + 1, ", ", aux + i, ">") # pentru a determina unde se afla cea verticala
            raspuns = input()
            if raspuns == "a":  # La intalnirea primului a inseamna ca zona b a fost depasita si a fost gasita linia verticala
                self.vertical = i + aux - 1
                break


    def colt4(self): # Functia colt1 care determina care sunt coordonatele linilor, cea verticala si orizontala in cazul in care
                     # zona b este in coltul 4 ( dreapta jos )
        for i in range(9):
            print("<", 9-i, ", ", 9-i, ">")   # interogheaza jucatorul x in privinta coordonatelor de pe diagonala cu coltul 4
            raspuns = input()
            if raspuns == "a":  # La intalnirea primului a inseamna ca zona b a fost depasita si a fost gasita linia orizontala
                self.orizontal = 9 - i  # Linia orizontala este egala cu pozitia liniei ( pe axa y )
                aux = 9 - i + 1  # Se foloseste un auxiliar pentru a retine coordonata unde se afla anterior coloana (pe axa x )
                break
        for i in range(aux):  # Stiind coordonata orizontala este interogat jucatorul despre coodronatele din stanga
            print("<",self.orizontal + 1, ", ", aux - i - 1,">") # pentru a determina unde se afla cea verticala
            raspuns = input()
            if raspuns == "a":  # La intalnirea primului a inseamna ca zona b a fost depasita si a fost gasita linia verticala
                self.vertical= aux - i - 1
                break