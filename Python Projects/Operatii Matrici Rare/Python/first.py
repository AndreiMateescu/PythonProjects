from metode import *

#Meniul este improvizat. Sunt convins ca se putea face mult mai bine
#insa principalul task a fost ca acele metode sa fie corecte si sa returneze rezultatul corect/functioneze corect
#Inmultirea este un caz particular, pentru a evita suprascrierea de date, trebuie sa creez 2 matrici cu numarul de linii si coloane adecvat

#daca numarul de coloane ale celei de-a 2-a matrici sunt diferite de numarul de linii al primeia nu se poate face inmultirea

#Prima data trebuie create matricile, ca sa putem folosi oricare dintre optiuni.
#La creare cand introduc elementul il introduc ca pe un sir
#De exemplu: 1 2 8.54 -> linia 1, coloana 2, valoarea 8.54

lines = int(input('Enter the number of lines: '))
columns = int(input('Enter the number of columns: '))
matrix_one = create(lines,columns)
matrix_two = create(lines,columns)

print('Menu\n 1. Show matrice\n 2. Dimensions\n 3. Addition\n 4. Diference\n 5. Multiplication\n 6. Acces element - value\n 7. Acces element - line and column\n 8. Unit matrice\n 9. Zero matrice\n 10. Transp. matrice')
option = int(input('Your option: '))

while option != 0:
    if option == 1:
        print_matrice(matrix_one,lines,columns)
        print_matrice(matrix_two,lines,columns)
    if option == 2:
        print('Lines:',lines,'Columns:',columns)
    if option == 3:
        matrix_three = addition(matrix_one,matrix_two,lines,columns)
        print_matrice(matrix_three,lines,columns)
    if option == 4:
        matrix_three = diference(matrix_one,matrix_two,lines,columns)
        print_matrice(matrix_three, lines, columns)
    if option == 5:
        print('1. First matrice', '2. Second matrice') #1-> caut in matricea 1, 2-> caut in matricea 2
        auxliar = int(input('Enter the option: '))
        if auxliar == 1:
            acces_elements_value(matrix_one,lines,columns)
        else:
            acces_elements_value(matrix_two,lines,columns)
    if option == 6:
        print('1. First matrice', '2. Second matrice') #1-> caut in matricea 1, 2-> caut in matricea 2
        auxliar = int(input('Enter the option: '))
        if auxliar == 1:
            acces_element(matrix_one)
        else:
            acces_element(matrix_two)
    if option == 7:
        matrix_four = create_unit(lines) #matrice unitate dupa numarul de linii. Puteam sa o creez si dupa numarul de coloana
        print_matrice(matrix_four,lines,lines)
    if option == 8:
        print('Number of elements sets to 0')
        matrix_four = create(lines,columns)
        print_matrice(matrix_four,lines,columns)
    if option == 9:
        print('1. First matrice', '2. Second matrice') #1-> transpusa primeia, 2-> transpusa celei de-a 2-a
        auxliar = int(input('Enter the option: '))
        if auxliar == 1:
            matrix_one = trans_matrice(matrix_one,lines,columns)
            print_matrice(matrix_one,lines,columns)
        else:
            matrix_two = trans_matrice(matrix_two,lines,columns)
            print_matrice(matrix_two,lines,columns)
    option = int(input('Your option: '))


#Inmultirea am facut-o ca un caz particular
print('Do you want to simulate multiplication? ')
print('\n1.Yes \n2.No')

x = int(input('Your option: '))
if x == 1:
    lines1 = int(input('Number of lines for multiplication for first matrice: '))
    columns1 = int(input('Number of columns for multiplication for first matrice: '))
    lines2 = int(input('Number of lines for multiplication for second matrice: '))
    columns2 = int(input('Number of columns for multiplication for second matrice: '))
    if columns1 != lines2:
        print('Error')
    else:
        lines = lines1
        columns = columns2
        matrix_one = create(lines1,columns1)
        print_matrice(matrix_one, lines1, columns1)
        matrix_two = create(lines2,columns2)
        print_matrice(matrix_two,lines2,columns2)

        matrix_three = multiplication(matrix_one,matrix_two,lines1,columns1,columns2)
        print_matrice(matrix_three,lines,columns)
else:
    if x == 2:
        print("You didn't want to simulate")