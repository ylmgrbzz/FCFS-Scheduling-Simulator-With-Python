print("FIRST COME FIRST SERVE SCHEDULLING")  # İlk Gelen İlk Hizmet Algoritması (FCFS) ile CPU zamanlama.
n= int(input("Enter number of processes : "))  # Kullanıcıdan toplam işlem sayısını girmesi isteniyor.
d = dict()  # İşlemleri ve ilgili zaman bilgilerini saklamak için bir sözlük (dictionary) oluşturuluyor.
 
for i in range(n):  # Kullanıcının belirttiği sayıda işlem için döngü başlatılıyor.
    key = "P"+str(i+1)  # İşlemler "P1", "P2", ... şeklinde isimlendiriliyor.
    a = int(input("Enter arrival time of process"+str(i+1)+": "))  # Kullanıcıdan işlemin varış zamanı (arrival time) alınıyor.
    b = int(input("Enter burst time of process"+str(i+1)+": "))  # Kullanıcıdan işlemin çalışma süresi (burst time) alınıyor.
    l = []  # Bu işlem için varış ve çalışma süresini saklamak amacıyla bir liste oluşturuluyor.
    l.append(a)  # Varış zamanı listeye ekleniyor.
    l.append(b)  # Çalışma süresi listeye ekleniyor.
    d[key] = l  # İşlem ismi (key) ve liste (value) sözlüğe ekleniyor.
 
# İşlemleri varış zamanına (arrival time) göre sıralıyoruz.
d = sorted(d.items(), key=lambda item: item[1][0])  
 
ET = []  # Çıkış zamanlarını (Exit Time) saklamak için bir liste.
for i in range(len(d)):  # Sıralı işlemler üzerinde döngü.
    if(i==0):  # Eğer ilk işlemse:
        ET.append(d[i][1][1])  # Çıkış zamanı sadece ilk işlemin çalışma süresine eşit olur.
    else:  # Diğer işlemler için:
        ET.append(ET[i-1] + d[i][1][1])  # Bir önceki işlemin çıkış zamanına bu işlemin çalışma süresi eklenir.
 
TAT = []  # Döngü zamanı (Turn Around Time) değerlerini saklamak için bir liste.
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])  # TAT = Çıkış Zamanı - Varış Zamanı
 
WT = []  # Bekleme Zamanı (Waiting Time) değerlerini saklamak için bir liste.
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])  # WT = Döngü Zamanı - Çalışma Süresi
 
# Ortalama bekleme zamanını hesaplıyoruz.
avg_WT = 0
for i in WT:  # Tüm bekleme zamanlarını topluyoruz.
    avg_WT += i
avg_WT = (avg_WT/n)  # Toplam bekleme zamanı işlem sayısına bölünüyor.
 
# İşlem detaylarını tablo şeklinde yazdırıyoruz.
print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
for i in range(n):
      print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
# Ortalama bekleme zamanı ekrana yazdırılıyor.
print("Average Waiting Time: ",avg_WT)
