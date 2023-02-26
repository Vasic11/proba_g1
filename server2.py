import socket,os,time,threading

s = socket.socket()
s.bind(("0.0.0.0", 8000))
s.listen()

def obrada(klijent,adresa):
    print("Slusanje...")
    klijent,adresa = s.accept()
    print(f"Stigao je zahtev sa adrese {adresa}")

    # time.sleep(10)

    pitanje = klijent.recv(4096).decode()
    pitanje = pitanje.split("\r\n\r\n")
    zaglavlje = pitanje[0].split("\r\n")
    metod,fajl,verzija = zaglavlje[0].split(' ')
    print(metod, fajl, verzija)
    fajl = fajl.lstrip("/")

    odgovor = ""

    if not fajl:
        odgovor = f"{verzija} 200 Ok\r\nContent-type: text/html\r\n\r\n"
        odgovor += open("index.html","r").read()
    elif not os.path.exists(fajl):
        odgovor = f"{verzija} 404 Not Found\r\n\r\n"
    else:
        odgovor = f"{verzija} 200 Ok\r\nContent-type: text/html\r\n\r\n"
        odgovor += open(fajl,"r").read()
        klijent.send(odgovor.encode())

while True:
    print("Slusanje...")
    klijent,adresa = s.accept()
    nova_nit = threading.Thread(None,obrada,args=(klijent,adresa))
    nova_nit.start()   