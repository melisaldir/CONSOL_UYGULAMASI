def hmmenu():
    print("╔══════════════════════════╗")
    print("║HESAP MAKİNESİ            ║")
    print("║1-Toplama                 ║")
    print("║2-Çıkarma                 ║")
    print("║3-Çarpma                  ║")
    print("║4-Bölme                   ║")
    print("║5-Bölümden kalan hesaplama║")
    print("║6-Çıkış (e)               ║")
    print("║  seçiminiz nedir?        ║")
    print("╚══════════════════════════╝")
    secim = input("Seçiminiz nedir?")
    if secim == "1" :
        x=input("1. sayıyı seçiniz")
        y=input("2. sayıyı seçiniz")
        print(int(x)+int(y))
    if secim == "2" :
        x=input("1. sayıyı seçiniz")
        y=input("2. sayıyı seçiniz")
        print(int(x)-int(y))
        hmmenu()
    if secim == "3" :
        x=input("1. sayıyı seçiniz")
        y=input("2. sayıyı seçiniz")
        print(int(x)*int(y))
        hmmenu()
    if secim == "4" :
        x=input("1. sayıyı seçiniz")
        y=input("2. sayıyı seçiniz")
        print(int(x)/int(y))
        hmmenu()
    if secim == "5" :
        x=input("1. sayıyı seçiniz")
        y=input("2. sayıyı seçiniz")
        print(int(x)%int(y))
        hmmenu()
    if secim == "6" :
        print("anamenüye yönlendirildiniz")
    
    
