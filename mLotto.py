#/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

liczba = random.randint(1, 10)


for i in range (10):
    odp = input("Jaką liczbę od 1 do 10 masz na myśli ? ")

    if liczba == int(odp) :
        print("podałeś:", odp)
        print("wylosowana", liczba)
        print("zgadłeś")
        break
    else:
        print("podałeś:", odp)
     #  print("wylosowana", liczba)
        print("niezgadłeś")


