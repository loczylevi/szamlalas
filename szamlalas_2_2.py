"""2.2 Feladat
A program számolja össze, hogy hány darab 'E' vagy 'e' betűt tartalmazó szó van az adott listában (amely a 'Próbáld ki!' gombra kattintva elérhető)! A képernyőre írja is ki a feltételnek megfelelő szavakat!"""

szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']

e_lista = []
szamlalo = 0
meddig = len(szavak) - 1
index = 0
for betu in szavak:
  index = 0
  for bet in betu:
    if bet == "e" or bet == "E":
      e_lista.append(betu)
      szamlalo = szamlalo + 1
    index = index + 1

halmaz = set(e_lista)

print(f"\"e\"-t vagy \"E\"-t tartalmazó szavak: {', '.join(halmaz)}\n szavak száma: {len(halmaz)}")

     
  
