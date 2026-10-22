#Ask1

import random

def Μαντεψε():
    y=random.randint(1,100)
    Trial =0

    print("Καλωσ ηρθες στο παιχνιδι μαντεψιας")
    print("Εχω σκεφτει εναν αριθμο απο το 1 στο 100.Μπορεις να τον βρεις;")

    while True:
        try:
             
            x = int(input("Δωσε την προβλεψη σου:"))
            Trial +=1

            if x > y: 
                print('Ο αριθμος ειναι μικροτερος')
            elif x < y:
                print("Ο αριθμος ειναι μεγαλυτερος")
            else :
                print("Μπραβο" ,y, f"ειναι ο σωστος αριθμος το βρηκες με {Trial} προσπαθειες")
                break

        except Value.Error:
            print(" Δεν τον βρηκες.Δωσε αλλο αριθμο:")
Μαντεψε()
