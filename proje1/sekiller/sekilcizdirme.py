import turtle

def kare():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

def ucgen():
    for x in range(3):
        turtle.forward(100)
        turtle.right(120)

def dikdortgen():
    for z in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

def besgen():
    for y in range(5):
        turtle.forward(100)
        turtle.right(72)

def altigen():
    for k in range(6):
        turtle.forward(100)
        turtle.right(60)
        
def cizimmenu():
    print("╔══════════════════════════╗")
    print("║ŞEKİL ÇİZDİRME            ║")
    print("║1-Kare                    ║")
    print("║2-Eşkenar Üçgen           ║")       
    print("║3-Dikdörtgen              ║")
    print("║4-Düzgün Beşgen           ║")
    print("║5-Düzgün Altıgen          ║")
    print("║6-Çıkış (e)               ║")
    print("║  seçiminiz nedir?        ║")
    print("╚══════════════════════════╝")
    secim = input("seçimini gir")
    if secim == "1" : kare()
    if secim == "2" : ucgen()
    if secim == "3" : dikdortgen()
    if secim == "4" : besgen()
    if secim == "5" : altigen()
