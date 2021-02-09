# Created and coded by Esref Zeki PARLAK

"""
PROJE 2 / İkinci Hafta
----------------------------
CUSTOMER LIFETIME VALUE PREDICTION PROJESİ
----------------------------
Proje detayları ve firma istekleri burada yer almaktadır:
https://drive.google.com/file/d/1PyzF5oibzfYVFHOAfPFhgWRjITtDYeDX/view?usp=sharing

İŞ PROBLEMİ - AMAÇ:

* GÖREV - 1:

BGNBD ve GG Modellerini kullanarak CLTV tahmini yapınız.

2010-2011 UK müşterileri için 6 aylık CLTV prediction yapınız.

- Elde ettiğiniz sonuçları yorumlayıp üzerinde değerlendirme yapmaya çalışınız veæ
mantıksız ya da çok isabetli olduğunu düşündüğünüz sonuçları vurgulayınız.

- Dikkat! 6 aylık expected sales değil cltv prediction yapılmasını bekliyoruz.
Yani direk bgnbd ve gamma modellerini kurarak devam ediniz ve
cltv prediction için ay bölümüne 6 giriniz.


* GÖREV - 2:

2010-2011 UK müşterileri için 1 aylık ve 12 aylık CLTV hesaplayınız.

1 aylık CLTV'de en yüksek olan 10 kişi ile 12 aylık'taki en yüksek 10 kişiyi analiz

ediniz. Fark var mı? Varsa sizce neden olabilir? Yorumlamaya çalışınız.

Dikkat! Sıfırdan model kurulmasına gerek yoktur, var olan bgf ve ggf üzerinden

direk cltv hesaplanabilir.


* GÖREV - 3:

1. 2010-2011 UK müşterileri için 6 aylık CLTV'ye göre tüm müşterilerinizi 3 gruba
(segmente) ayırınız ve grup isimlerini veri setine ekleyiniz. Örneğin (A, B, C)

- 3 grubu veri setindeki diğer değişkenler açısıdan analiz ediniz.

- 3 grup için yönetime 6 aylık aksiyon önerilerinde bulununuz. Kısa kısa.

2. top_flag adında bir değişken oluşturunuz. CLTV'ye göre en iyi yüzde 20'yi

seçiniz ve bu kişiler için top_flag 1 yazınız. Diğerlerine 0 yazınız.

"""