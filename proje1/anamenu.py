import hesaplamalar.hesapmakinesi
import sekiller.sekilcizdirme
import saglık.saglık
import oyunlar.oyun
import hesaplamalar.harfnot
import sıcaklık.sicaklikdonustur
import takvim.takvimaylar
import carpimtablo.carpımtablosu
import ders.derstakibi
def anamenu():
    print("╔═══════════════════╗")
    print("║   VEKTOREL DERS   ║")
    print("║1-Hesap Makinesi   ║")
    print("║2-Şekil Çizdirme   ║")
    print("║3-Sağlık           ║")
    print("║4-Oyunlar          ║")
    print("║5-Not Hesaplama    ║")
    print("║6-Ders Takibi      ║")
    print("║7-Çarpım Tablosu   ║")
    print("║8-Takvim           ║")
    print("║9-Döviz Uygulaması ║")
    print("║10-Sıcaklık Çevirme║")
    print("║11-Çıkış (e)       ║")
    print("║  seçiminiz nedir? ║")
    print("╚═══════════════════╝")
    secim = input("Seçiminiz nedir?")
    if secim == "1" :
        hesaplamalar.hesapmakinesi.hmmenu()
        anamenu()
    if secim == "2" :
        sekiller.sekilcizdirme.cizimmenu()
        anamenu()
    if secim == "3":
        saglık.saglık.saglıkmenu()
        anamenu()
    if secim =="4":
        oyunlar.oyun.oyunmenu()
        anamenu()
    if secim =="5":
        hesaplamalar.harfnot.harfnotu()
        anamenu()
    if secim =="6":
        ders.derstakibi.dtmenu()
        anamenu()
    if secim =="7":
        carpimtablo.carpımtablosu.ctmenu()
        anamenu()
    if secim =="8":
        takvim.takvimaylar.takvimmenu()
        anamenu()
    if secim =="9":
        hesaplamalar.harfnot.harfnotu()
        anamenu()
    if secim =="10":
        sıcaklık.sicaklikdonustur.sdmenu()
        anamenu()
    if secim == "11": exit()
    else:
        print("Seçim sadece 1,2,3,4,5,6,7,8,9,10,11 olabilir.")
        anamenu()
    
anamenu()