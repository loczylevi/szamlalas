"""1. Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!"""

import random
lista = []
for szam in range(5):
  veletlen = random.randint(1,10)
  lista.append(veletlen)

paros_szam = [szam for szam in lista if szam % 2 == 0]

print(f"Az 5 db. generált szám: {lista}\n A páros számok száma: {len(paros_szam)}\n a Páros számok: {paros_szam}")