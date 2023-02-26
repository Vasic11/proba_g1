import threading,time


# x = []

poruka = ["",""]


katanac = threading.Lock() #Zakljucavamo negde i tek kada se zavrsi druga funkzija moze da pocne


def f(broj):
        # global x    #Global se odnosi na x izvan funkcije
        # x.append(broj)
        # print(f"Hello {x}")
    global poruka
    katanac.acquire()
    print(broj, poruka)
    poruka[0] = broj
    poruka[1] = broj + 1
    print(broj, poruka)
    katanac.release()


for i in range(100):
    threading.Thread(None,f,args=(i,)).start()      #args