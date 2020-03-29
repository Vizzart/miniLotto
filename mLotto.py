#/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

liczba = random.randint(1, 10)

odp = input ("Jaką liczbę od 1 do 10 masz na myśli ? ")

print("podałeś:", odp)

print ("wylosowana", liczba)

if liczba == int(odp) :
    print("zgadłeś")
else:
    print("niezgadłeś")



