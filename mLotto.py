# /usr/bin/env python3
# -*- coding: utf-8 -*-


import random

number = random.randint(1, 10)

for i in range(3):
    print()
    print("Proba", i + 1)
    answer = int (input("Jaką liczbę od 1 do 10 masz na myśli ? "))
    if answer < 0 or answer > 10:
        print("zakres")
    else:
        if number == int(answer):

            print("podałeś:", answer)
            print("wylosowana", number)
            print("zgadłeś")
            break
        elif i == 2:
            print()
            print("podałeś:", answer)
            print("Miałem na myśli liczbe", number)
        else:
            print("podałeś:", answer)
            print("niezgadłeś, sprobuj ponownie")
