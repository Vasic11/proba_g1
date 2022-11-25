import random

kurs = "Python fundamentals"
print(kurs)

a = 10
b = 5
print("Oduzimanje:", a - b)
print("Sabiranje:", a + b)


rez_mnozenja = a * b
print("Mnozenje:", rez_mnozenja)

rez_deljenje = a / b
print("Deljenje:", int(rez_deljenje))

a = 5
b = 2

print(5 / 2)
print(5 // 2)

print(10 // 3)

print(a ** 2) # 5 * 5
print(a ** 3) # 5 * 5 * 5

a = 10
b = 2

# Koji je ostatak pri deljenju sa dva - nema ostatka
print(10 % 2)

# Koji je ostatak pri deljenju sa dva - ostatak je 1
a = 9
b = 2
print(a % b) # ovde se dobija samo ostatak pri deljenju

print(-a)

godine = 25
# godine + 1
            # 26
godine = godine + 1
print(godine)

godine += 1 # uvecaj i dodeli jedan za godine
print(godine)

godine *= 2 # mnozi i dodeljuje
print(godine)
godine * 2 # mnozi ali ne dodeljuje

godine //= 2 # delji i daje ceo broj
print(godine)


# broj1 = 10
# broj2 = 5

# print("Pvri broj:", broj1)
# print("Drugi broj:", broj2)

# print("Rezultat:", broj1 + broj2)
            # unos iz konzole
# broj1 = input("Unesi prvi broj: ")
# # "40" -> 40
# broj2 = input("Unesite drugi broj: ")

# print("Sabiranje: ", int(broj1) + int(broj2))

# postavljanje vrednosti
# pi = 3.14
# povrsina_kruga = 0

# r = float(input("Unesite r: "))

# povrsina_kruga = r ** 2 * pi
# print("Povrsina kruga je:", povrsina_kruga)

# godine = 18

# print(godine <= 18)

# print(godine != 18) # razlicito
# print(godine == 18)

# aktuelan_kurs = "PPF"

# print(aktuelan_kurs == "PPF")

# broj = int(input("Unesite breoj: "))

# ostatak = broj % 2
# print(ostatak == 0) # ako je print 0 ostatak onda je paran


# moj_broj = int(input("Unesite broj: "))
# racunar = random.randint(1, 10)

# print("Korisnik: ", moj_broj)
# print("Racunar: ", racunar)

# print("Pogodak: ", moj_broj == racunar)

# automobil_pozicija = 0
# cilj_pozicija = 50

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# korisnik1 = int(input("Unesite godine: "))

# print("Allowed - ", korisnik1 >= 13)

# sifra == uneta sifra
# uneto_ime = "admin1"
# uneta_sifra = "123456"

# ime_baza = "admin"
# sifra_baza = "12345"

# ispravna_sifra = uneta_sifra == sifra_baza
# ispravna_kor_ime = uneto_ime == ime_baza

# uspesno_logovanje =ispravna_sifra and ispravna_kor_ime
# print(uspesno_logovanje)

'''

and

true true -> true
true false -> false

or
 true true -> true
 true false -> true
 false false -> false
'''


uneto_ime = "admin"
uneta_sifra = "123456"

ime_baza = "admin"
sifra_baza = "12345"

ispravna_sifra = uneta_sifra == sifra_baza
ispravna_kor_ime = uneto_ime == ime_baza

uspesno_logovanje =ispravna_sifra or ispravna_kor_ime
print(uspesno_logovanje)


lepo_vreme = True
print(not lepo_vreme)

tamna_tema = True
print(not tamna_tema)

# unos smea - tekst
# unos generacija - int

#DA LI JE POGODJEN SMER I DA LI POGODJENA GENERACIJA
#smer    Python
#generacija  2022
# True / False

unos_smera = input("Uneso smer: ")
unos_generacije = int(input("Uneti generciju: "))

smer = "Python"
generacija = 2022

logovanje = unos_smera == smer and unos_generacije == generacija
print(logovanje)