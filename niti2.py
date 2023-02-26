import threading,random,time
zaustaviti_nit = False
def game():
    i1 = 0
    i2 = 0
    while i1 < 10 and i2 < 10:
        if zaustaviti_nit:
            return
        print(f"Rezultat {i1} : {i2}")
        i1 += random.randint(0,1)
        i2 += random.randint(0,1)
        time.sleep(1)   
    else:
        if i1 == 10 and i2 == 10:
            print("Nereseno je.")
        else:
            print("Pobedink je","i1" if i1 == 10 else "i2")     

niti1 = threading.Thread(None,game)
niti1.start()
time.sleep(3)
zaustaviti_nit = True