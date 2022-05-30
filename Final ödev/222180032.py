# -----------------------------------------------------------------------------------------------------------------------------------
#                                BİLGİSAYARDA PROGRAMLAMA FİNAL PROJESİ --- BASİT QUİZ PROGRAMI
# -----------------------------------------------------------------------------------------------------------------------------------
#                      Mustafacan Beyhan - 222180032 - github.com/mbyhn1
#  GRUP ÜYELERİ:       Muhammet Ali Yılmaz - 222180028 - github.com/Muhammetali16
#                      Yusuf Cenk - 222180059 - github.com/yycenk
# -----------------------------------------------------------------------------------------------------------------------------------

import time
import sys                                      # PROGRAMDA KULLANILAN MODÜLLERİN TANITILDIĞI SATIRLAR
from pygame import mixer

mixer.init()
mixer.music.load("muzik.mp3")                     # MÜZİĞİ TANITMAYA YARAYAN KOD
mixer.music.set_volume(0.03)                      # MÜZİK SES AYARI
mixer.music.play()                                # PROGRAM BAŞLATILDIĞI ZAMAN MÜZİĞİ BAŞLATACAK KOD


print("SORULAR GELİYOR, HAZIRLAN!")

for i in range(3,0,-1):
    time.sleep (1)                               # OYUN BAŞLAMADAN ÖNCE 3 SANİYE SÜRECEK KISA BİR GERİ SAYIM
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()

def yeni_oyun():                                 # OYUNU BAŞLATMAK İÇİN GEREKLİ OLAN FONKSİYON 

    tahminler = []
    dogru_tahminler = 0
    soru_numarasi = 1

    for key in sorular:
        
        time.sleep(0.5)                          # SORULAR ARASINDA YARIM SANİYE GECİKME 
        
        print("-------------------------")
        print(key)
        
        for i in cevaplar[soru_numarasi-1]:
            
            print(i)
           
# -----------------------------------------------------------------------------------------------------------------------------------

        tahmin = input("Enter (A, B, C, D): ")
        tahmin = tahmin.upper()
        tahminler.append(tahmin)         
        dogru_tahminler += cevap_kontrol(sorular.get(key), tahmin)
        soru_numarasi += 1  

    display_score(dogru_tahminler, tahminler)
        
# -----------------------------------------------------------------------------------------------------------------------------------
def cevap_kontrol(cevap, tahmin):                    # CEVAPLARI KONTROL ETMEK İÇİN GEREKLİ OLAN FONKSİYON
        
    if cevap == tahmin:
        print("DOĞRU CEVAP!")                        # CEVAP SÖZLÜKTE BELİRTİLEN ŞIKLA AYNI İSE EKRANA DOĞRU YAZDIR
        return 1
    else:
        print("YANLIŞ CEVAP!")                       # CEVAP SÖZLÜKTE BELİRTİLEN ŞIKLA AYNI DEĞİL İSE EKRANA YANLIŞ YAZDIR
        return 0
    
# -----------------------------------------------------------------------------------------------------------------------------------
def display_score(dogru_tahminler, tahminler):              # PUANI GÖSTERMEK İÇİN GEREKLİ OLAN FONKSİYON

    
    print("-------------------------")
    print("SONUÇLAR")
    print("-------------------------")
    
    print("Cevaplar: ", end="")
    for i in sorular:
        print(sorular.get(i), end=" ")
    print()

    print("Tahminler: ", end="")
    for i in tahminler:
        print(i, end=" ")
    print()

    score = int((dogru_tahminler/len(sorular))*100)
    print("Skorun: "+str(score)+"%")
    
    

# -----------------------------------------------------------------------------------------------------------------------------------
def tekrar_oyna():                 # OYUNA TEKRAR BAŞLAMAK İÇİN GEREKLİ OLAN FONKSİYON

    response = input("Tekrar oynamak ister misin? (evet veya hayır): ")
    response = response.upper()          # CEVAPTA KÜÇÜK YA DA BÜYÜK HARF AYRIMI OLMAMASI İÇİN

    if response == "EVET":               
        return True                     # KULLANICININ CEVABI EVET İSE PROGRAM BAŞA DÖNER HAYIR İSE PROGRAM SONLANIR
    else:
        return False
# -----------------------------------------------------------------------------------------------------------------------------------

# SORULARIN VE DOĞRU CEVAPLARIN BULUNDUĞU SÖZLÜK
sorular = {
 "1- İnternet üzerinden görüntülü konuşma amacıyla kullanılan bilgisayar donanımı aşağıdakilerden hangisidir?: ": "B", 
 "2- Bilgisayarın elle tutulabilen ve gözle görülebilen kısımlarına ne ad verilir?: ": "A",
 "3- Aşağıdaki yazılımlardan hangisi sistem yazılımıdır?: ": "D",
 "4- Bilgisayardaki tüm işlemlerin yapıldığı dahili donanım birimi hangisidir?: ": "C",
 "5- Bilgisayarın çalışma hızını belirleyen donanım birimleri hangileridir? I-Anakart II-Ram III-İşlemci IV-Güç Kaynağı: ": "C",
 "6- Aşağıdakilerden hangisi dahili donanım birimidir?: ": "B",
 "7- Aşağıdaki uygulama yazılımlarından hangisi yanlış eşleştirilmiştir?: ": "D",
 "8- İnternete bağlanmamızı sağlayan donanım birimi aşağıdakilerden hangisidir?: ": "A",
 "9- Müzik dinlemek için kullandığımız uygulama yazılımı aşağıdakilerden hangisidir?: ": "D",
 "10- Aşağıdakilerden hangisi bir sistem yazılımıdır?: ": "C",
 "11- Bilgisayardaki tüm bilgilerimizin kalıcı olarak depolandığı donanım birimi hangisidir?: ": "B",
 "12- Aşağıdakilerden hangileri harici donanım birimidir? I-Sabit Disk II-Modem III-Ağ Kartı IV-Ekran: ": "C",
 "13- Aşağıdakilerden hangisi internete girmek için kullandığımız yazılımlardan değildir?: ": "B",
 "14- Bir resmi, şekli veya yazıyı bilgisayara aktarmaya yarayan donanım birimi aşağıdakilerden hangisidir?: ": "B",
 "15- Özellikle yeni çıkmış bilgisayar oyunlarını oynarken bilgisayarın hızını etkileyen donanım birimi hangisidir?: ": "B"
}

# -----------------------------------------------------------------------------------------------------------------------------------

# CEVAPLARIN BULUNDUĞU SÖZLÜK
cevaplar =[["A. Tarayıcı", "B. Web kamerası", "C. Yazıcı", "D. Ekran"],
          ["A. Donanım", "B. Sistem yazılımı", "C. Uygulama yazılımı", "D. Donatım"],
          ["A. Google Chrome", "B. Paint", "C. Avira Antivirüs", "D. Windows 10"],
          ["A. Ana kart","B. Ram", "C. İşlemci", "D.  Sabit Disk"],
          ["A. I ve II","B. I ve III", "C. II ve III", "D. III ve IV"],
          ["A. Kasa","B. Anakart", "C. Ekran", "D. Tarayıcı"],
          ["A. Eset Nod 32 - Antivirüs Yazılımı","B. Mozilla Firefox - İnternet Tarayıcısı", "C. Paint - Resim Programı", "D. Microsoft Word - Sunum Programı"],
          ["A. Modem","B. Anakart", "C. İşlemci", "D. Ses kartı"],
          ["A. Paint","B. Microsoft Powerpoint", "C. Avira", "D. Winamp"],
          ["A. Google Chrome","B. Internet Explorer", "C. Adobe Photoshop", "D. Windows XP"],
          ["A. Anakart","B. Sabit Disk", "C. Ekran Kartı", "D. Bellek"],
          ["A. II ve III","B. III ve IV", "C. II ve IV", "D. I ve IV"],
          ["A. Internet Explorer","B. Macromedia Fireworks", "C. Opera", "D. Yandex Browser"],
          ["A. Tarayıcı","B. Aktarıcı", "C. Yazıcı", "D. Oyun konsolu"],
          ["A. Ana Kart","B. Ekran Kartı", "C. Sabit Disk", "D. Ağ Kartı"]]

# -----------------------------------------------------------------------------------------------------------------------------------

yeni_oyun()

while tekrar_oyna():
    yeni_oyun()

print("Program kapatılıyor...")
for i in range(3,0,-1):
    time.sleep (0.05)
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(0.5)
