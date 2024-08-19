import random

def tas_kagit_makas_ADINIZ_SOYADINIZ(): # Oyun kuralları - giriş ekranı
    print("""
          Taş, Kağıt, Makas oyununa hoşgeldiniz.
          Kurallar:
            - Taş kağıdı yener, kağıt makası yener, makas taşı yener.
            - İlk iki turu kazanan oyunu kazanır.
            - Oyun bittikten sonra tekrar oynamak isterseniz devam edecektir.
            - Çıkmak için 'hayır' yazın.
          """)


    secenekler = ["taş", "kağıt", "makas"]
    oyun_sayaci = 0
    oyuncu_galibiyet = 0
    bilgisayar_galibiyet = 0
    
    while True: # Oyuncu ve bilgisayarın turlarını sıfırladığımız yer
        tur_sayaci = 0
        oyuncu_skor = 0
        bilgisayar_skor = 0        
        print("\nYeni oyun başlıyor!")
        

        while oyuncu_skor < 2 and bilgisayar_skor < 2:
            
            oyuncu_secimi = input("\nTaş, kağıt veya makas seçin: ").lower() # Oyuncu seçim yapıyor eğer büyük ifade girerse .lower() ile küçülteceğiz
           
            while oyuncu_secimi not in secenekler:
                oyuncu_secimi = input("Lütfen taş, kağıt veya makastan birini seçin!! ").lower()

            
            bilgisayar_secimi = random.choice(secenekler) # Bilgisayar rastgele bir seçim alıyor
            print(f"Bilgisayar {bilgisayar_secimi} seçti.")

            if oyuncu_secimi == bilgisayar_secimi: # Turu kim kazandı onu belirleme
                print("Berabere kaldınız.")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu kazandınız!")
                oyuncu_skor += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_skor += 1

            tur_sayaci += 1  # tur takibi ve ekrana sonuç yazdırma kısmı
            print(f"Oynanan tur sayısı: {tur_sayaci}")
            print(f"Skor: Oyuncu {oyuncu_skor} - {bilgisayar_skor} Bilgisayar")


        if oyuncu_skor == 2: # galibi belirliyoruz
            print("\nTebrikler! Oyunu kazandınız.")
            oyuncu_galibiyet += 1
        else:
            print("\nBilgisayar oyunu kazandı.")
            bilgisayar_galibiyet += 1

        oyun_sayaci += 1 # toplam oynanan oyun sayısı ve galibiyetleri tuttuğumuz yer
        print(f"Oynanan oyun sayısı: {oyun_sayaci}")
        print(f"Genel Skor: Oyuncu {oyuncu_galibiyet} - {bilgisayar_galibiyet} Bilgisayar")


        devam_etme = input("\nBaşka bir oyun oynamak ister misin? (evet/hayır): ").lower() # Oyuna devam edilecekmi onun kontrolü
        if devam_etme != "evet":
            print("Güle güle.")
            break


        bilgisayar_devam_istegi = random.choice(["evet", "hayır"]) # Bilgisayara random değer vererek devam etmek istiyormu ona bakıyoruz
        print(f"Bilgisayar {bilgisayar_devam_istegi} demeyi seçti.")
        if bilgisayar_devam_istegi != "evet":
            print("Bilgisayar oynamak istemiyor.. :D")
            break

if __name__ == "__main__":
    tas_kagit_makas_ADINIZ_SOYADINIZ()
