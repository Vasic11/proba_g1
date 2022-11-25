import random
# sekunde = 10
#     #True \ False
# while sekunde > 0:
#     #True
#     print(sekunde)
#     sekunde -= 1 #9 8 7 6 5 4 3 2 1

# #False

# while True:
#     print("Cao")

# baterija

# baterija = 90

# while baterija > 0:
#     print("Mozete koristiti uredjaj, baterija:", baterija, "%")
#     baterija -= random.randint(5, 15)

# print("Baterija je prazna...")


# zivoti 5 sve dok su zivoti veci od 0 kad su 0 igra je zavrsena

# zivot = 5
# while zivot > 0:
#     print("Igra jos traje, ostalo vam je jos ", zivot, "zivota.")
#     zivot -= random.randint(1, 3)

# print("Igra je gotova.")

# for zivot in range(5, 0, -1):
#     print("Igra traje")

# print("Igra je gotova")


# broj_pokusaja = 7
# poeni = 0


# while broj_pokusaja > 0:
#     srecan_broj = random.randint(1, 20)
#     moj_broj = int(input("Unesite broj: "))

#     if srecan_broj == moj_broj:
#         print("Pogodak.", "Moj broj", moj_broj, "Srecan broj:", srecan_broj)
#         poeni += 1
#         break
#     else:
#         print("Promasaj.", "Moj broj", moj_broj, "Srecan broj:", srecan_broj)
#         broj_pokusaja -= 1


# print("Igra je gotova, poeni:", poeni)

# for broj in range(1, 10):
#     print(broj)
#     if broj == 5:
#         break

# #continue
# #stamaj sve osim 3
# for broj in range(1, 10):
#     if broj == 3:
#         continue
#     print(broj)

# for ime in ["petar", "marko", "jovana", "katarina", "ana"]:
#     if ime == "milica":
#         print("Pronadjena!")
#         break
#     print(ime)
# else:
#     print("Zavrseno citanje polaznika...")


zbir = 0


while True:
    broj = input("Unesite neki broj: ")

    if broj == "":
        print("Zbir je: ", zbir)
    elif broj.isnumeric():
        zbir += int(broj)
    elif broj == "quit":
        exit(0)
    else:
        print("Proverite unos.")
