#KULLANICIYA MENÜYÜ GÖSTEREN VE DEĞER DÖNDÜRMEYEN FONKSİYON
def menu_goruntule():
    print("-----MENÜ-----")
    print("1.Fal Bakma Oyunu ♥♠♦♣")
    print("2.Blackjack (21) Oyunu ♥♠♦♣")
    print("3.Çıkış (→→→)" )
#MENÜDE SEÇİM YAPARKEN SAYI ALAN FONKSİYON
def sayi_alma(alt_sinir,ust_sinir):
    sayi=int(input())
    while sayi<alt_sinir or sayi>ust_sinir:
        sayi=int(input("Menü dahilinde olmayan bir sayı girdiniz,lütfen tekrar giriniz:"))
    return sayi
#BLACKJACK İÇİN KART DEĞELERİNİ BULAN FONKSİYON
def kart_degeri(kart):
        if kart[:1] in ("V","K","P","1"):  #VALE-KIZ-PAPAZ ÇIKTIĞINDA DEĞERİ 10 ALINACAKTIR
            return int(10)
        elif kart[:1] in ("2","3","4","5","6","7","8","9"):
            return int(kart[:1])
        elif kart[:1] == 'A':   #AS ÇIKTIĞINDA OYUNCUYA SEÇİMİ SORULACAKTIR(1 veya 11)
            print("Yerden gelen kağıt:"+ str(kart))
            sayi_onay=input("1 olarak mı yoksa 11 olarak mı kullanmak istiyorsunuz?:")
            while sayi_onay=="1" or sayi_onay =="11":
                if sayi_onay== '1':
                    return int(1)
                    break
                elif sayi_onay == '11':
                    return int(11)
                    break
                else:
                    sayi_onay=input("1 olarak mı yoksa 11 olarak mı kullanmak istiyorsunuz?")
#GENEL PROGRAM DÖNGÜSÜNÜ SAĞLAYACAK FONKSİYON
def menu():
    cikis='h'
    while cikis=='H' or cikis=='h':
        menu_goruntule()
        print("Yukarıdaki menüye göre seçiminizi giriniz [1-3]:",end='')
        secim=sayi_alma(1,3)
        if secim==1:
            fal_bakma_oyunu()
            oyun_onay=input("Aynı oyunu tekrar oynamak istiyor musunuz(e/E/h/H)?:")
            while oyun_onay not in ['e', 'E', 'h', 'H']:  #GENEL HATA KONTROLÜ YAPAN DÖNGÜ
                oyun_onay=input("Hatalı giriş yaptınız,lütfen tekrar giriniz(e/E/h/H)?:")
            if oyun_onay=="e" or oyun_onay=="E":
                fal_bakma_oyunu()
        elif secim==2:
            blackjack_oyunu()
            oyun_onay=input("Aynı oyunu tekrar oynamak istiyor musunuz(e/E/h/H)?:")
            while oyun_onay not in ['e', 'E', 'h', 'H']:  #GENEL HATA KONTROLÜ YAPAN DÖNGÜ
                oyun_onay=input("Hatalı giriş yaptınız,lütfen tekrar giriniz(e/E/h/H)?:")
            while oyun_onay=="e" or oyun_onay=="E":
                blackjack_oyunu()
                oyun_onay=input("Aynı oyunu tekrar oynamak istiyor musunuz(e/E/h/H)?:")
        else:
            cikis=input("Çıkmak istediğinize emin misiniz(e/E/h/H)?:")
            while cikis not in ['e', 'E', 'h', 'H']:
                cikis=input("Hatalı giriş yaptınız,lütfen tekrar giriniz:")
#FAL BAKMA OYUNU FONKSİYONU
def fal_bakma_oyunu():
    cevap=input("Niyetinizi tuttunuz mu(e/E/h/H)?:")
    while cevap not in ['e', 'E', 'h', 'H']:  #NİYET TUTMA SORUSUNDA GENEL HATA KONRTOLÜ YAPAN DÖNGÜ
        cevap=input("Hatalı giriş yaptınız,lütfen tekrar giriniz(e/E/h/H)?:")
    while cevap=="H" or cevap=="h":    #NİYET TUTMA SORUSUNDA EVET-HAYIR SORUSUNU KONTROL EDEN DÖNGÜ VE BURDA HATA KONTROLÜ YAPAN DÖNGÜ
        print("Fal bakma oyununun amacı bir niyet tutup bu niyetin gerçekleşme olasılığını bulmaktır!.")
        print("Lütfen yukarıdaki bilgiyi göz önünde bulundurunuz")
        cevap=input("Niyetinizi tuttunuz mu(e/E/h/H)?:")
        if cevap not in ['e', 'E', 'h', 'H']:
            cevap=input("Hatalı giriş yaptınız,lütfen tekrar giriniz(e/E/h/H)?:")
        elif cevap=="e" or cevap=="E":
            break
        else:
            print("Fal bakma oyununun amacı bir niyet tutup bu niyetin gerçekleşme olasılığını bulmaktır!.")
            print("Lütfen yukarıdaki bilgiyi göz önünde bulundurunuz")
            cevap=input("Niyetinizi tuttunuz mu(e/E/h/H)?:")
    import random
    simgeler = ["Karo","Maça","Sinek","Kupa"]   #OYUN İÇİN İSKAMBİL DESTESİ HAZIRLANIR
    sayilar = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    kagitlar=[]
    for simge in simgeler:
        for sayi in sayilar:
            kagitlar.append(simge + " " + str(sayi))
    random.shuffle(kagitlar)
    kagit_toplam = 0
    while(len(kagitlar) > 0): #OYUNUN KAĞITLAR BİTENE KADAR SÜRMESİNİ SAĞLAYAN DÖNGÜ
        sayac = 0
        kalan = []
        for x in range(0, min(len(kagitlar), 13)): #HER 13 KAĞIT İÇİN SAYMA YAPAN DÖNGÜ
            kalan.append(kagitlar[x])
            sayac += 1
            #KAĞIDIN SIRA NUMARASIYLA EŞLEMESİ DURUMU
            if kalan[x] == "Karo " + str(x+1) or kalan[x] == "Maça " + str(x+1) or kalan[x] =="Kupa " + str(x+1) or kalan[x] =="Sinek " + str(x+1):
                y=input("{}. {}".format(str(x+1),kalan[x]))
                print("*** Yukarıdaki kağıt sıra numarasıyla eşleşti,kağıtlar saymaya yeniden başlanıyor. ***")
                if x+1 > 10:
                    kagit_toplam+=10
                else:
                    kagit_toplam+=x+1
                kalan.pop(x)
                kagitlar.extend(kalan)
                break
            #KAĞIDIN SIRA NUMARASIYLA EŞLEŞMEMESİ DURUMU
            else:
                x=input(("{}. {}".format(str(x+1),kalan[x])))
        if sayac==13:
            x=input("*** Hiçbir kağıt eşleşmedi,saymaya yeniden başlanıyor. ***")
        for x in range(0, sayac):#DESTEYE SONDAN EKLENEN KAĞITLARI ÜSTTEN ÇIKARTAN DÖNGÜ
            kagitlar.pop(0)
    print("Niyetiniz %{} ihtimalle gerçekleşecektir.".format(str(kagit_toplam)))
    print("Oynadığınız için teşekkürler...  :)")
#BLACKJACK OYUNU FONKSİYONU
def blackjack_oyunu():
    import random
    simgeler = ["Karo","Maça","Sinek","Kupa"]  #OYUN İÇİN İSKAMBİL DESTESİ HAZIRLANIR
    sayilar = ["As",'2','3','4','5','6','7','8','9','10','Vale','Kız','Papaz']
    kagitlar=[]
    for simge in simgeler:
        for sayi in sayilar:
            kagitlar.append(sayi + " " + simge)
    dagitici_kart1 = random.choice(kagitlar) #DAĞITICI İÇİN 2 KAĞIT VERİLİR VE BİRİ YAZDIRILIR
    kagitlar.remove(dagitici_kart1)
    dagitici_kart2 = random.choice(kagitlar)
    kagitlar.remove(dagitici_kart2)
    dagitici_toplami = kart_degeri(dagitici_kart1) + kart_degeri(dagitici_kart1)
    print ("Dağıtıcının Açık Kağıdı: " + dagitici_kart1,"+ ???")
    kart1 = random.choice(kagitlar)   #OYUNCU İÇİN 2 KAĞIT VERİLİR VE YAZDIRILIR
    kagitlar.remove(kart1)
    kart2 = random.choice(kagitlar)
    kagitlar.remove(kart2)
    oyuncu_toplami = kart_degeri(kart1) +kart_degeri(kart2)
    print ("Oyuncunun Kağıtları:" + kart1 + "," + kart2)
    print("Oyuncunun Kart değerleri toplamı:" + str(oyuncu_toplami))
    if oyuncu_toplami == 21:#OYUNCU İLK ELDEN BLACKJACK YAPARSA DİREK KAZANIR!
        print("Oyuncu Blackjack yaptı!")
    else:
        while oyuncu_toplami < 21:  #EĞER OYUNUNCUNUN ELİ 21DEN KÜÇÜK İSE OYUNCUYA SORULAN SORUNUN CEVABINA GÖRE DÖNGÜ
            cevap = input("(K)ağıt mı, (P)as mı?:")
            #OYUNCU KAĞIT İSTERSE YENİ BİR KAĞIT VERİLİP YENİ TOPLAM BULUNUR
            if cevap=="k" or cevap=="K":
                oyuncunun_aldigi_kagit =random.choice(kagitlar)
                kagitlar.remove(oyuncunun_aldigi_kagit)
                alinanan_yeni_kagidin_degeri = kart_degeri(oyuncunun_aldigi_kagit)
                oyuncu_toplami += int(alinanan_yeni_kagidin_degeri)
                print("Yeni gelen kağıt:",oyuncunun_aldigi_kagit)
                print("Yeni kağıt sonucu oyuncunun kağıt toplamı:" + str(oyuncu_toplami))
                #YENİ ALININ KAĞIT SONUCU YENİ TOPLAMA GÖRE OLABİLECEK DURUMLAR VE DÖNDÜRDÜĞÜ DEĞERLER
                if oyuncu_toplami > 21:
                    print("Oyuncu Kaybetti.")
                elif oyuncu_toplami == 21:
                    print("Oyuncu Blackjack yaptı!")
                else:
                    continue
                #OYUNCU SORUYA PAS DERSE OLUŞACAK DURUMLAR
            elif cevap== "P" or cevap=="p":
                if dagitici_toplami < 17: #EL TOPLAMI 17DEN KÜÇÜKSE DAĞITICIYA BİR KAĞIT VERİLİR VE DAĞITICI TOPLAMI BULUNUR
                    print("Dağıtıcı bir kağıt daha ister.")
                    dagiticinin_aldigi_kagit = random.choice(kagitlar)
                    kagitlar.remove(dagiticinin_aldigi_kagit)
                    dagiticinin_aldigi_kagit_degeri = kart_degeri(dagiticinin_aldigi_kagit)
                    dagitici_toplami += int(dagiticinin_aldigi_kagit_degeri)
                    print("Dağıtıcıya verilen yeni kağıt: " + str(dagiticinin_aldigi_kagit))
                    if dagitici_toplami < 21 and dagitici_toplami > oyuncu_toplami: #OLUŞAN YENİ TOPLAMA GÖRE OLUŞACAK DURUMLAR
                        print("Dağıtıcı toplamı:" + str(dagitici_toplami))
                        print("Oyuncu kaybetti.")
                    elif dagitici_toplami > 21 and oyuncu_toplami <=21:
                        print("Dağıtıcı battı,Oyuncu kazandı.")
                    else:
                        continue
                elif dagitici_toplami < oyuncu_toplami: #DAĞITICININ EL TOPLAMI EN BAŞTA 17DEN BÜYÜKSE OLUŞACAK DURUMLAR
                    print("Dağıtıcının kart değerleri toplamı:",dagitici_toplami)
                    print("Oyuncunun kart değerleri toplamı:",oyuncu_toplami)
                    print("Oyuncu Kazandı.")
                elif dagitici_toplami == oyuncu_toplami:
                    print("Dağıtıcının kart değerleri toplamı:",dagitici_toplami)
                    print("Oyuncunun kart değerleri toplamı:",oyuncu_toplami)
                    print("Beraberlik.")
                else:
                    print("Dağıtıcının kart değerleri toplamı:",dagitici_toplami)
                    print("Oyuncunun kart değerleri toplamı:",oyuncu_toplami)
                    print("Oyuncu Kaybetti.")
                break
    print("Oynadığınız için teşekkürler...  :)")
menu()

            #SERGEN KARATAŞ - MERT GÜLBAHÇE
            #05150000637    - 05150000684
