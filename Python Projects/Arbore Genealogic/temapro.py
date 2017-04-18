import time

class Familie:

    def __init__(self, tip_barbat = 0, nume_barbat = 0, prenume_barbat = 0, tip_femeie = 0, nume_femeie = 0, prenume_femeie = 0, data_casatorie = 0):
        self.__tip_barbat = tip_barbat
        self.__tip_femeie = tip_femeie
        self.__nume_barbat = nume_barbat
        self.__prenume_barbat = prenume_barbat
        self.__nume_femeie = nume_femeie
        self.__prenume_femeie = prenume_barbat
        self.__data_casatoriei = data_casatorie

    def set_nume_barbat(self,__x):
        self.__nume_barbat = __x

    def set_prenume_barbat(self,__x):
        self.__prenume_barbat = __x

    def set_tip_barbat(self,__x):
        self.__tip_barbat = __x

    def set_nume_femeie(self, __x):
        self.__nume_femeie = __x

    def set_prenume_femeie(self, __x):
        self.__prenume_femeie = __x

    def set_tip_femeie(self, __x):
        self.__tip_femeie = __x

    def set_data_casatoriei(self, __x):
        self.__data_casatoriei = __x

    def get_nume_barbat(self):
        return self.__nume_barbat

    def get_prenume_barbat(self):
        return self.__prenume_barbat

    def get_tip_barbat(self):
        return self.__tip_barbat

    def get_nume_femeie(self):
        return self.__nume_femeie

    def get_prenume_femeie(self):
        return self.__prenume_femeie

    def get_tip_femeie(self):
        return self.__tip_femeie

    def get_data_casatoriei(self):
        return self.__data_casatoriei

    def __str__(self):
        return self.__tip_barbat + ' : ' + self.__nume_barbat + ' ' + self.__prenume_barbat + ' ' + self.__tip_femeie + ' : ' + self.__nume_femeie + ' ' + self.__prenume_femeie + ' ' + self.__data_casatoriei

class Nastere():

    def __init__(self, tip_copil = 0, nume_tata = 0, prenume_fiu = 0,  data_nasterii = 0):
        self.__tip_copil = tip_copil
        self.__nume_tata = nume_tata
        self.__prenume_fiu = prenume_fiu
        self.__data_nasterii = data_nasterii

    def set_nume_tata(self,__x):
        self.__nume_tata = __x

    def set_prenume_fiu(self,__x):
        self.__prenume_fiu = __x

    def set_data_nasterii(self, __x):
        self.__data_nasterii = __x

    def set_tip_copil(self, __x):
        self.__tip_copil = __x

    def get_nume_tata(self):
        return self.__nume_tata

    def get_prenume_fiu(self):
        return self.__prenume_fiu

    def get_data_nasterii(self):
        return self.__data_nasterii

    def get_tip_copil(self):
        return self.__tip_copil

    def __str__(self):
        return self.__tip_copil + ' : ' + self.__prenume_fiu + ' ' + self.__data_nasterii

class Ruda():

    def set_nume_ruda(self,__x):
        self.__nume_ruda = __x

    def set_prenume_ruda(self, __x):
        self.__prenume_ruda = __x

    def set_tip_ruda(self, __x):
        self.__tip_ruda = __x

    def get_nume_ruda(self):
        return self.__nume_ruda

    def get_prenume_ruda(self):
        return self.__prenume_ruda

    def get_tip_ruda(self):
        return self.__tip_ruda

    def __str__(self):
        return self.__tip_ruda + ' : ' + self.__nume_ruda + ' ' + self.__prenume_ruda

class Divort():

    def set_nume_sot(self, __x):
        self.__nume_sot = __x

    def set_prenume_sot(self, __x):
        self.__prenume_sot = __x

    def set_nume_sotie(self, __x):
        self.__nume_sotie = __x

    def set_prenume_sotie(self, __x):
        self.__prenume_sotie = __x

    def set_data_divort(self, __x):
        self.__data_divort = __x

    def set_tip_divortat(self, __x):
        self.__divortat = __x

    def get_nume_sot(self):
        return self.__nume_sot

    def get_prenume_sot(self):
        return self.__prenume_sot

    def get_nume_sotie(self):
        return self.__nume_sotie

    def get_prenume_sotie(self):
        return self.__prenume_sotie

    def set_tip_divortata(self, __x):
        self.__divortata = __x

    def get_data_divort(self):
        return self.__data_divort

    def get_tip_divortat(self):
        return self.__divortat

    def get_tip_divortata(self):
        return self.__divortata

    def __str__(self):
        return self.__divortat + ' : ' + self.__nume_sot + ' ' + self.__prenume_sot + ' ' + self.__divortata + ' : ' + self.__nume_sotie + ' ' +  self.__prenume_sotie + ' ' + self.__data_divort


relatii_casatorie = [] #aici formez o lista de obiecte de tip Familie
relatii_rude = [] #lista de obiecte de tip Ruda
relatii_nastere = [] #lista de obiecte de tip Nastere

afisare = [] #o lista de obiecte generale, cu ajutorul ei afisez lucrurile care ma intereseaza

lista_rude = [] #lista de liste (fara obiecte). Cu ajutorul ei, rezolv punctul c.
lista_nascuti = [] #lista de liste pentru c)

n = int(input('Numarul de familii: '))

casatoriti = [] #lista de casatoriti ca sa imi dau seama mai usor de cine este casatorit si cine nu
descendenti_total = [] #lista de liste normala (nu este de obiecte) cu toate rudele, soti, copii. O sublista contine tot pentru o familie

for i in range(n):
    familie = Familie()
    descendenti = [] #lista pentru o familie, o s-o adaug in descendenti_total
    rude = [] #lista cu obiectele de tip Ruda pentru o familie, o s-o adaug in relatii rude
    nascuti_cuplu_actual = [] #lista pentru o familie cu copiii, o s-o adaug in lista_nascuti
    copii = [] #lista cu obiecte de tip nastere, pe care o adaug in relatii_nastere

    desparte_rude = [] #lista de rude pentru o familie (nu sunt obiecte), o s-o adaug in lista_rude


    sotn = input('Numele sotului: ')
    sotp = input('Prenumele sotului: ')
    sotien = input('Numele sotiei: ')
    sotiep = input('Prenumele sotiei: ')
    data = input('Data casatoriei: ')

    familie.set_nume_barbat(sotn)
    familie.set_prenume_barbat(sotp)
    familie.set_nume_femeie(sotien)
    familie.set_prenume_femeie(sotiep)
    familie.set_data_casatoriei(data)
    familie.set_tip_barbat('Sot')
    familie.set_tip_femeie('Sotie')

    casatoriti.append(sotn)
    casatoriti.append(sotp)
    casatoriti.append(sotien)
    casatoriti.append(sotiep)

    option = input('Barbatul are rude: ')
    while option == 'Da' or option == 'da' or option == 'DA':
        rude_aux = []
        rude_barbat = Ruda()
        tip_ruda = input('Tip ruda: ')
        nume = input('Nume ruda: ')
        prenume = input('Prenume ruda: ')

        rude_barbat.set_tip_ruda(tip_ruda)
        rude_barbat.set_nume_ruda(nume)
        rude_barbat.set_prenume_ruda(prenume)

        rude_aux.append(tip_ruda)
        rude_aux.append(nume)
        rude_aux.append(prenume)

        desparte_rude.append(rude_aux)

        descendenti.append(nume)
        descendenti.append(prenume)

        rude.append(rude_barbat)
        afisare.append(rude_barbat)
        option = input('Barbatul mai are rude: ')

    option = input('Femeia are rude: ')
    while option == 'Da' or option == 'da' or option == 'DA':
        rude_aux = []
        rude_femeie = Ruda()
        tip_ruda = input('Tip ruda: ')
        nume = input('Nume ruda: ')
        prenume = input('Prenume ruda: ')

        rude_femeie.set_tip_ruda(tip_ruda)
        rude_femeie.set_nume_ruda(nume)
        rude_femeie.set_prenume_ruda(prenume)

        rude_aux.append(tip_ruda)
        rude_aux.append(nume)
        rude_aux.append(prenume)

        desparte_rude.append(rude_aux)

        descendenti.append(nume)
        descendenti.append(prenume)

        rude.append(rude_femeie)
        afisare.append(rude_femeie)
        option = input('Femeia mai are rude: ')

    descendenti.append(sotn)
    descendenti.append(sotp)
    descendenti.append(sotien)
    descendenti.append(sotiep)

    afisare.append(familie)

    lista_rude.append(desparte_rude)

    mostenitor = input('Au mostenitori? ')
    if mostenitor == 'DA' or mostenitor == 'da' or mostenitor == 'Da':
        cati = int(input('Cati? '))
        for j in range(cati):
            fii = []
            copil = Nastere()

            copil.set_tip_copil('Copil')
            prenume = input('Dati prenumele copilului: ')
            copil.set_prenume_fiu(prenume)
            copil.set_nume_tata(familie.get_nume_barbat())

            data_nasterii = input('Dati data nasterii: ')
            copil.set_data_nasterii(data_nasterii)

            descendenti.append(prenume)
            afisare.append(copil)
            copii.append(copil)

            fii.append(copil.get_tip_copil())
            fii.append(copil.get_nume_tata())
            fii.append(copil.get_prenume_fiu())
            nascuti_cuplu_actual.append(fii)

    lista_nascuti.append(nascuti_cuplu_actual)
    relatii_rude.append(rude)
    relatii_casatorie.append(familie)
    relatii_nastere.append(copii)
    descendenti_total.append(descendenti)

for element in afisare:
    print(element)

divortati = []
divortat = input('A divortat cineva? ')
while divortat == 'Da' or divortat == 'da' or divortat == 'DA':
    nume_barbat = input('Dati numele sotului: ')
    prenume_barbat = input('Dati prenumele sotului: ')
    nume_femeie = input('Dati numele sotiei: ')
    prenume_femeie = input('Dati prenumele sotiei: ')

    ok = False
    OK = False
    okay = False
    total_ok = False

    for element in casatoriti:
        if element == nume_barbat:
            print('Gasit')
            ok = True
            break

    for element in casatoriti:
        if element == prenume_barbat:
            print('Gasit')
            OK = True
            break

    for element in casatoriti:
        if element == nume_femeie:
            print('Gasita')
            okay = True
            break

    for element in casatoriti:
        if element == prenume_femeie:
            print('Gasita')
            total_ok = True
            break

    if ok == True and OK == True and okay == True and total_ok == True:
        casatoriti.remove(nume_barbat)
        casatoriti.remove(prenume_barbat)
        casatoriti.remove(nume_femeie)
        casatoriti.remove(prenume_femeie)

        div = Divort()
        div.set_prenume_sot(prenume_barbat)
        div.set_nume_sot(nume_barbat)
        div.set_prenume_sotie(prenume_femeie)
        div.set_nume_sotie(nume_femeie)
        data_divort = input('Data divortului: ')
        div.set_data_divort(data_divort)
        div.set_tip_divortat('Divortat')
        div.set_tip_divortata('Divortata')

        divortati.append(div)
        divortat = input('A mai divortat cineva? ')
    else:
        print('N-au fost gasiti')
        divortat = input('A mai divortat cineva? ')

print(casatoriti)

for element in relatii_casatorie:
    print(element)
print('\n')

for element in divortati:
    print(element)

print('\nPauza 5 secunde')
time.sleep(5)

#a) Starea Civila
print('Starea civila a unei persoane la o anumita data')
time.sleep(2)

nume_persoana = input('Dati numele persoanei: ')
prenume_persoana = input('Dati prenumele persoanei: ')
print('Dati data: ')
z = int(input('Ziua: '))
l = int(input('Luna: '))
a = int(input('Anul: '))

ok_casatorita = False
ok_divortata = False

for i in range(len(relatii_casatorie)):
    if (relatii_casatorie[i].get_nume_barbat() == nume_persoana and relatii_casatorie[i].get_prenume_barbat() == prenume_persoana) or (relatii_casatorie[i].get_nume_femeie() == nume_persoana and relatii_casatorie[i].get_prenume_femeie() == prenume_persoana):
        ok_casatorita = True
        pozitie1 = i
        break

for j in range(len(divortati)):
    if (divortati[j].get_nume_sot() == nume_persoana and divortati[j].get_prenume_sot() == prenume_persoana) or (divortati[j].get_nume_sotie() == nume_persoana and divortati[j].get_prenume_sotie() == prenume_persoana):
        ok_divortata = True
        pozitie2 = j
        break

if ok_casatorita == True and ok_divortata == False:
    zi_casatorie, luna_casatorie, an_casatorie = relatii_casatorie[pozitie1].get_data_casatoriei().split(' ')

    if a < int(an_casatorie):
        print('Necasatorita')
    if a == int(an_casatorie):
        if l < int(luna_casatorie):
            print('Necasatorita')
        else:
            if l > int(luna_casatorie):
                print('Casatorita')
            else:
                if l == int(luna_casatorie):
                    if z < int(zi_casatorie):
                        print('Necesatorita')
                    else:
                        print('Casatorita')
    if a > int(an_casatorie):
        print('Casatorita')

if ok_casatorita == True and ok_divortata == True:
    zi_casatorie, luna_casatorie, an_casatorie = relatii_casatorie[pozitie1].get_data_casatoriei().split(' ')
    zi_divort, luna_divort, an_divort = divortati[pozitie2].get_data_divort().split(' ')
    if a < int(an_casatorie):
        print('Necasatorita')
    if a == int(an_casatorie) and a < int(an_divort):
        if l < int(luna_casatorie):
            print('Necasatorita')
        else:
            if l > int(luna_casatorie):
                print('Casatorita')
            else:
                if l == int(luna_casatorie):
                    if z < int(zi_casatorie):
                        print('Necesatorita')
                    else:
                        print('Casatorita')

    if a > int(an_casatorie):
        if a < int(an_divort):
            print('Casatorita')
        if a == int(an_divort):
            if l < int(luna_divort):
                print('Casatorita')
            if l > int(luna_divort):
                print('Divortata')
            if l == int(luna_divort):
                if z < int(zi_divort):
                    print('Casatorita')
                else:
                    print('Divortata')
        if a > int(an_divort):
            print('Divortata')

    if int(an_casatorie) == int(an_divort):
        if l < int(luna_casatorie):
            print('Necesatorita')
        if l > int(luna_casatorie) and l < int(luna_divort):
            print('Casatorita')
        if l > int(luna_divort):
            print('Divortata')
        if l == int(luna_divort) and l == int(luna_casatorie):
            if z < int(zi_casatorie):
                print('Necasatorita')
            elif z > int(zi_casatorie) and z < int(zi_divort):
                print('Casatorita')
            elif z > int(zi_divort):
                print('Divortata')
            if z == int(zi_casatorie):
                print('Casatorita')
            if z == int(zi_divort):
                print('Divortata')

if ok_casatorita == False and ok_divortata == False:
    print('Persoana nu exista, deci necasatorita')

#b)
print('Descendentii unei persoane specificate')
time.sleep(2)

print(descendenti_total)
print('\n')
nume_pers_desc = input('Nume persoana: ')
prenume_pers_desc = input('Prenume persoana: ')

poz_lista1 = -1
poz_lista2 = -1
for i in range(len(descendenti_total)): #i pozitia sublistei
    for j in range(len(descendenti_total[i])):
        if descendenti_total[i][j] == nume_pers_desc:
            poz_lista1 = i
            poz_nume = j
            break

for i in range(len(descendenti_total)):
    for j in range(len(descendenti_total[i])):
        if descendenti_total[i][j] == prenume_pers_desc:
            poz_lista2 = i
            poz_prenume = j
            break

if poz_lista1 == -1 and poz_lista2 == -1:
    print('Nu s-au gasit in aceeasi lista')
else:
    if poz_lista1 == poz_lista2:
        print(descendenti_total[poz_lista1][poz_prenume+1:])
    else:
        print('Nu se poate')

#c)
print('Relatiile intre 2 persoane specificate')
time.sleep(2)

print('Rude: ')
print(lista_rude)
print('Copii: ')
print(lista_nascuti)

nume1 = input('Numele primei persoane: ')
prenume1 = input('Prenumele primei persoane: ')
nume2 = input('Numelei celeilalte persoane: ')
prenume2 = input('Prenumele celeilalte persoane: ')
print('Se va da raspunsul depinzand de sot/sotie. Se cunoaste mai intai relatia persoane cu sot/sotie')
time.sleep(5)

def cauta(nume,prenume):
    ok_final = False
    for i in range(len(relatii_casatorie)):
        if relatii_casatorie[i].get_nume_barbat() == nume and relatii_casatorie[i].get_prenume_barbat() == prenume:
            ok_final = True
            return relatii_casatorie[i].get_tip_barbat(),i

        if relatii_casatorie[i].get_nume_femeie()  == nume and relatii_casatorie[i].get_prenume_femeie() == prenume:
            ok_final = True
            return relatii_casatorie[i].get_tip_femeie(),i

    for i in range(len(divortati)):
        if divortati[i].get_nume_sot() == nume and divortati[i].get_prenume_sot() == prenume:
            ok_final = True
            return divortati[i].get_tip_divortat(),i
        if divortati[i].get_nume_sotie() == nume and divortati[i].get_prenume_sotie() == prenume:
            ok_final = True
            return divortati[i].get_tip_divortata(),i

    for i in range(len(lista_rude)):
        for j in range(len(lista_rude[i])):
            if lista_rude[i][j][1] == nume and lista_rude[i][j][2] == prenume:
                return lista_rude[i][j][0], i

    for i in range(len(lista_nascuti)):
        for j in range(len(lista_nascuti[i])):
            if lista_nascuti[i][j][1] == nume and lista_nascuti[i][j][2] == prenume:
                return lista_nascuti[i][j][0], i

    if ok_final == False:
        return 'Nu exista','Nu exista'


data1,pozitie1 = cauta(nume1,prenume1)
data2,pozitie2 = cauta(nume2,prenume2)
if pozitie1 == pozitie2:
    if data1 == 'Divortat' or data1 == 'Divortata' or data2 == 'Divortat' or data2 == 'Divortata':
        print('Nu sunt rude')
    else:
        print('Rude')
        if ((data1 == 'Tata' and data2 == 'Sot') or (data1 == 'Sot' and data2 == 'Tata')) and nume1 == nume2:
            print('Tata si fiu')
        elif ((data1 == 'Tata' and data2 == 'Sotie') or (data1 == 'Sotie' and data2 == 'Tata')) and nume1 == nume2:
            print('Tata si fiica')
        elif ((data1 == 'Tata' and data2 == 'Mama') or (data1 == 'Mama' and data2 == 'Tata')) and nume1 == nume2:
            print('Soti')
        elif ((data1 == 'Frate' and data2 == 'Tata') or (data1 == 'Tata' and data2 == 'Frate')) and nume1 == nume2:
            print('Tata si fiu')
        elif ((data1 == 'Sora' and data2 == 'Tata') or (data1 == 'Tata' and data2 == 'Sora')) and nume1 == nume2:
            print('Tata si fiica')
        elif ((data1 == 'Frate' and data2 == 'Mama') or (data1 == 'Mama' and data2 == 'Frate')) and nume1 == nume2:
            print('Mama si fiu')
        elif ((data1 == 'Sot' and data2 == 'Mama') or (data1 == 'Mama' and data2 == 'Sot')) and nume1 == nume2:
            print('Mama si fiu')
        elif ((data1 == 'Mama' and data2 == 'Sora') or (data1 == 'Sora' and data2 == 'Mama')) and nume1 == nume2:
            print('Mama si fiica')
        elif ((data1 == 'Frate' and data2 == 'Sot') or (data1 == 'Sot' and data2 == 'Frate')) and nume1 == nume2:
            print('Frati')
        elif ((data1 == 'Sora' and data2 == 'Sot') or (data1 == 'Sot' and data2 == 'Sora')) and nume1 == nume2:
            print('Frate si sora')
        elif ((data1 == 'Sora' and data2 == 'Sotie') or (data1 == 'Sotie' and data2 == 'Sora')) and nume1 == nume2:
            print('Surori')
        else:
            print('Alta rudenia apropiata')

        print(data1, 'pentru sot/sotie')
        print(data2, 'pentru sot/sotie')
else:
    print('Nu sunt rude')