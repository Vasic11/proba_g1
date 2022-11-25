import random
# x = 10

#  print(x > 0)
#  print("x je vece od 0")
#     #True
# if x > 0:
#     print("x je vece od 0")
#     print("ja sam u if bloku koda")
#     print("evo ovde se zavrsava")

# print("ova linija se izvrasava u svakom slucaju...")

# godine = 13

# if godine >= 13:
#     print("korisnik ima vise od 13 godina.")

# vozilo_se_krece = False
# brzina = 40
#     #True
# if vozilo_se_krece: # ako je vozilo se krece True
#     print("Vozilo se krece... proveri i brzinu")
#     if brzina > 50:
#         print("Prekoracena brzina")
#     if brzina <= 50:
#         print("Brzina je OK.")



proizvod = "Laptop"
cena = 500

# 1 - prikaz proizvoda ; 2 - kupi; 3 - izlaz
# stanje = int(input("Unesite stanje na racunu: "))
# komanda = int(input("Unesite komandu: "))

# if komanda == 1:
#     print("Proizvod:", proizvod,"Cena:", cena)
# if komanda == 2:
#     print("Pristupili ste kupovini.")
#     if stanje >= cena:
#         print("Uspesna kupovina.")
#     else:
#         print("Neuspesna kupovina.")
# if komanda == 3:
#     print("Izlaz.")
# # if komanda != 1 and  komanda != 2 and komanda != 3:
# if komanda < 1 or komanda > 3:
#     print("Unesite 1, 2 ili 3.")

# broj = -5
#     # uslov
# if broj >= 0:
#     print("Broj je veci ili jednak 0.") # uslov True
# else:
#     print("Broj je manji od 0.")    # uslov False


# uspesno_logovnje = True

# if uspesno_logovnje:
#     print("Otvori pocetnu stranu.")
# else:
#     print("Proverite podatke.")

# number = 10
# if number % 2 == 0:
#     print("Broj je paran")
# else:
#     print("Broj je neparan")


# baterija = 85
# punjac = False

# if baterija > 0 or punjac:
#     print("Mozete koristiti telefon.")
# else:
#     print("Proverite stanje baterije.")


# num = 5

# if num > 0:
#     print("Broj je veci od 0.")
# elif num == 0:
#     print("Broj je 0.")
# elif num == 5:
#     print("Broj je bas 5.")
# else:
#     print("Broj je manje od 0.")


# redni_broj_u_nedelji = 1

# redni_broj_u_nedelji = int(input("Unesite redni broj u nedelji: "))

# if redni_broj_u_nedelji == 1:
#     print("Ponedeljak.")
# elif redni_broj_u_nedelji == 2:
#     print("Utorek.")
# elif redni_broj_u_nedelji == 3:
#     print("Sreda.")
# elif redni_broj_u_nedelji == 4:
#     print("Cetvrtak.")
# elif redni_broj_u_nedelji == 5:
#     print("Petak.")
# elif redni_broj_u_nedelji == 6:
#     print("Subota.")
# elif redni_broj_u_nedelji == 7:
#     print("Nedelja.")
# else:
#     print("Pogresan broj, unesite broj izmedju 1 i 7.")


# trenutna_vrednost = random.randint(1, 100)
# nova_vrednost = int(input("Unesite vrednost: "))

# print("Trenutna:", trenutna_vrednost, "Nova:", nova_vrednost)

# if nova_vrednost > trenutna_vrednost:
#     print("Postigli ste novi high score!!!")
# elif nova_vrednost == trenutna_vrednost:
#     print("Vredmosti su jednake.")
# else:
#     print("Nova vrednost je manja.")


# a = int(input("Unesi prvi broj: "))
# b = int(input("Unesite drugi broj: "))
# operacije = input("Unesite operaciju (+, -, *, /): ")

# if operacije == "+":
#     print("Rezulta:", a + b)
# elif operacije == "-":
#     print("Rezultet:", a - b)
# elif operacije == "*":
#     print("Rezultat:", a * b)
# elif operacije == "/":
#     print("Rezultat:", a / b)
# else:
#     print("Neispravna operacija.")
    

# poruka = ""
# pol = input("Unesite pol: ")

# # if pol == "m":
# #     poruka = "Hello mister"
# # else:
# #     poruka = "Hello miss"
#         # True              # Uslov     # False
# poruka = "Hello mister" if pol == "m" else "Hello miss"

# print(poruka)


poeni = 90 
izvestaj = ""
if poeni > 50:
    izvestaj = "Polozili ste ispit."
else:
    izvestaj = "Niste polozili"


izvestaj = "Polozili ste" if poeni > 50 else "Niste polozili"