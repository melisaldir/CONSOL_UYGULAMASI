def menumenu():
    print("╔══════════════════════════╗")
    print("║YEMEK ÖNERİLERİ           ║")
    print("║1-Çorba                   ║")
    print("║2-Ana Yemek               ║")
    print("║3-Yardımcı Yemek          ║")
    print("║4-Salata                  ║")
    print("║5-Tatlı                   ║")
    print("║6-Çıkış (e)               ║")
    print("║  seçiminiz nedir?        ║")
    print("╚══════════════════════════╝")
    secim = input("Seçiminiz nedir?")
    if secim == "1" :
        corba = ["Mercimek Çorbası","Domates Çorbası","Tavuk Suyu Çorbası","Yayla Çorbası"]
        print(corba)
    if secim == "2" :
        anayemekler = ["Karnabahar","Fasülye","Nohut","Tas Kebabı"]
        print(anayemekler)
    if secim == "3" :
        yyemekler = ["Pirinç Pilavı","Bulgur Pilavı","Erişte","Makarna"]
        print(yyemekler)
    if secim == "4" :
        salata = ["Çoban Salatası","Kaşık Salata","Patlıcan Salatası","Patates Salatası"]
        print(salata)
    if secim == "5" :
        tatli = ["Kalburabastı","Sütlaç","Islak Kek","Meyve Salatası"]
        print(tatli)
    if secim == "6" :
        print("anamenüye yönlendirildiniz")