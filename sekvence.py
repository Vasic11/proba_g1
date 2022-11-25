# osoba = ["marko", 25, "IOS"]
# print(osoba)

# print(osoba[0])
# print(osoba[1])
# print(osoba[2])

# for broj in range(5):
#     print(broj)

# for broj in range(5, 20):
#     print(broj)

# for broj in range(0, 31, 2):
#     print(broj)

# kurs = "Python"
# print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3])

# print(len(kurs)) #broj clanova

# for indeks in range(len(kurs)-1):
#     print(kurs[indeks])

# ustanova = "IT Academy"
# print(len(ustanova))

# for slovo in range(len(ustanova)-1):
#     print(ustanova[slovo])

# '''

#     for brojac in sekvenca:
#         ...
# '''

# for slovo in ustanova:
#     print(slovo)



# tip_korisnika = "admin"

# tip_korisnika[0] = "A"
    #lower -> admin    upper -> ADMIN
# korisnicko_ime = input("Unesite korisnicko ime: ")

# if korisnicko_ime.upper() == "admin1":
#     print("Dobrodosli")
# else:
#     print("Neispravni podaci")

# tekst  = "A*B#C#D"
#     # vrednost
# for slovo in tekst:
#     if slovo != "*" and slovo != "#":
#         print(slovo)

#     # idneks
# for x in range(len(tekst)-1):
#     if tekst[x] == "*":
#         print("* je na poziciji", x)
#     elif tekst[x] == "#":
#         print("# je na poziciji", x)
#     else:
#         print(tekst[x])

# slovo = "A"
# print(slovo in tekst)

# LISTA
telefoni = ["iPhone 11", "Samsung A22", "Huawei Mate 50"]

print(telefoni[1])

telefoni[0] = "iPhone 12 Pro"

# Ponuda telefona
for telefon in telefoni:
    print(telefon)

for indeks in range(len(telefoni)-1):
    #print(indeks)
    print(telefoni[indeks])

# sve dok je broj indeksa manji od rednog broja poslednjeg clana

indeks = 0
duzina_liste = len(telefoni)

while indeks < duzina_liste:
    print(telefoni[indeks])
    indeks += 1



# ponuda_smerova = ["python", "php", "ios", "java"]
# zeljeni_smer = input("Unesite zeljeni smer: ")
# #"python", "php", "ios", "java"
# for smer in ponuda_smerova:
#     if zeljeni_smer == smer:
#         print("Izabrali ste dobar smer")
#         break
#     else:
#         print("Niste odabrali smer.")

ponuda_smerova = ["python", "php", "ios", "java"]
ponuda_smerova.append("c#")

print(ponuda_smerova)

porba = []
porba.append(5)
porba.append("hello")

print(porba)
# porba.remove(5)   uklanja clan koji smo naveli
# porba.pop(0)      uklanja vrednost na tom indeksu
# porba.clear()     uklanja sve
del porba[0]       #uklanja indeks 

print(porba)

laptopvi = ["acer", "dell", "macbook"]

for i in range(len(laptopvi)):
    print(laptopvi[i])



for vrednost in laptopvi:
    print(vrednost)



for i, v in enumerate(laptopvi):
    print("Indeks:", i, "Vrednost:", v)


termini = ["ponedeljak", "sreda", "petak"]

for x in range(len(termini)):
    if "utorak" != termini[x]:
        print("Dodajte i utorak u spisak")
    print(termini[x])

if "utorak" in termini:
    print("Utorak je medju terminima")
else:
    print("Dodajte i utorak")

# if not "utorak" in termini:  da li se ne nalazi

smerovi = ["python", "php", "ios", "java", "c#", "frontend", "android"]
                        # pocetak kraj i korak
promocija = smerovi[1:4:2]
print(promocija)

#range (0 ,10, 2)


korisnici = ["petar", "marija", "jovana", "vladimir", "milos", "katarina"]

pobednici = korisnici[0: 3]
print(pobednici)
pobednici.clear()

for i in range(len(korisnici)):
    if i == 0 or i == 1 or i == 2:
        pobednici.append(korisnici[i])

print(pobednici)


brojevi = [1, 10, 7, 2, 6, 3, 17, 30]

parni = []
neparni = []


# for petlja
# % == 0
# append

for broj in brojevi:
    # parni.append(broj) if broj % 2 == 0 else neparni.append(broj):
    # print(broj)

    if broj % 2 == 0:
        parni.append(broj)
    else:
        neparni.append(broj)

print(parni)
print(neparni)



# rec = input("Unesite rec: ")
# pocetni_indek = 0
# krajnji_indeks = len(rec)-1
# palindrom = True
# '''
# rec[0] == rec[14]
# rec[1] == rec[13]
# rec[2] == rec[12]

# '''


# while pocetni_indek < krajnji_indeks:
#     if rec[pocetni_indek] != rec[krajnji_indeks]:
#         print("Nije palindrom.")
#         palindrom = False
#         break
#     pocetni_indek += 1
#     krajnji_indeks -= 1
# else:
#     print("Jeste palindrom.")


# print("Rec", rec, ("jeste" if palindrom else "nije"),  "palindrom")


kursevi = ["python", "ios", "design"]

# unos kursa input
# provera da li postoji u listi kurseva (in)
# append
# svaki put nako unosa ili poruke ispisati listu kurseva
while True:
    unos_kursa = input("Unesite kurs: ")

    if unos_kursa in kursevi:
        print("Vec postoji")
    else:
        kursevi.append(unos_kursa)

    # in proverava da li se nesto nalazi u sekvenci

# for kurs in kursevi:
#     if unos_kursa == kursevi:
#         print("Uneli ste dobar kurs.")
#         continue
# else:
#     kursevi.append(unos_kursa)
#     print(kursevi)






