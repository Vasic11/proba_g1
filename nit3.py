import threading,time,random

class CSMatch(threading.Thread):
    def __init__(self, i1, i2):
        super().__init__()
        self.player1 = i1
        self.player2 = i2
    
    
    
    def run(self):
        print(f"Hello from cs match {self.player1} vs {self.player2}")
        for i in range(5):
            print(f"{self.player1} vs {self.player2} {i}")
            time.sleep(1)

red = [
    ("Dovla", "Kristijan"),
    ("Vasa","Nicole"),
    ("Mica", "Adrana")
]

def gamer_runner():
    while True:
        while red and (igraci := red.pop(0)):
            partija = CSMatch(igraci[0], igraci[1])
            partija.start()


grthreath = threading.Thread(None,gamer_runner)
grthreath.start()

while True:
    red.append((input("First player: "),input("Second player: ")))