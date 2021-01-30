###############################################
# ÖDEVLER:
# ZORUNLU ODEV 1: Komut satırından Python kodu çalıştırma.
# ZORUNLU ODEV 2: Veri Okuryazarlığı Sertifika
# ZORUNLU ODEV 3: List Comprehension Applications
# KEYFİ ÖDEV 1: "setler" konusu izlenecek ve Python 101, 102, 103 sertifikaları alınacak.
# KEYFİ ÖDEV 2: Python scriptine konsoldan arguman vermek konusunu araştırınız ve bir örnek uygulama yapınız.
###############################################


###############################################
# ZORUNLU ODEV 1: Komut satırından Python kodu çalıştırma. ***YAPILDI***
###############################################

# Yazacak olduğunuz "py" uzantılı bir python dosyasını komut satırından çalıştırmanız beklenmektedir.
# Örneğin hi.py isimli bir dosyanız olsun ve içinde print("isim soy isim") kodu olsun.
# Bilgisayarınızın konsolunu açıp konsoldan hi.py dosyasının olduğu dizine gelip buradan "python hi.py" kodunu
# çalıştırdığınızda ekranınızda "isim soy isim" yazmalı.
# Adım adım nasıl yapılacağı anlatılmıştır.

# Adım 1: PyCharm'da "hi.py" isminde python dosyası oluştur.
# Adım 2: Bu dosyanın içirisine şu kodu kendine göre yaz ve kaydet: print("Ben Sinan Artun ÖDEV tamam, bu çok kolaymış")
# Adım 3: Şimdi konsoldan "hi.py" dosyasının olduğu dizine (klasöre) gitmen gerekiyor.
# Neyse ki PyCharm ile bu çok kolay. Sol tarafta yer alan menüde hi.py dosyası hangi klasördeyse
# o klasöre sağ tuş ile tıklayıp şu seçimi yap: "open in > terminal".
# PyCharm'ın alt tarafında terminal ekranı açılacak. Şu anda hi.py dosyası ile aynı dizindesin (klasörde).
# Adım 4: Konsolda şu kodu yazmalısın: python hi.py
# Adım 5: Çıktını ekran görüntüsünü alıp grubunda paylaş.


###############################################
# ZORUNLU ODEV 2: Veri Okuryazarlığı Sertifika  ****YAPILDI****
###############################################

# Aşağıdaki adreste yer alan "Veri Okuryazarlığı" sınavına girilecek ve sertifika alınacak.
# https://gelecegiyazanlar.turkcell.com.tr/konu/veri-okuryazarligi


###############################################
# ZORUNLU ODEV 3: List Comprehension Applications
###############################################

###############################################
# Görev 1: car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
###############################################

# Veri setini baştan okutarak aşağıdaki çıktıyı elde etmeye çalışınız.

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notlar:
# Numerik olmayanların da isimleri büyümeli.
# Tek bir list comp yapısı ile yapılmalı.


###############################################
# Görev 1 Çözüm
###############################################



###############################################
# Görev 2: İsminde "no" BARINDIRMAYAN değişkenlerin isimlerininin SONUNA "FLAG" yazınız.
###############################################

# Tüm değişken isimleri büyük olmalı.
# Tek bir list comp ile yapılmalı.

# Beklenen çıktı:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']


###############################################
# Görev 2 Çözüm
###############################################


###############################################
# Görev 3: Aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçerek yeni bir df oluşturunuz.
###############################################

# df.columns
# og_list = ["abbrev", "no_previous"]

# Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df["new_cols"] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.

# Beklenen çıktı:

# new_df.head()
#
#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630

###############################################
# Görev 3 Çözüm
###############################################


###############################################
# KEYFİ ÖDEV 1: (TAKİP EDİLMEYECEK - SORULAR YANITLANAMAYACAKTIR)
# Geleceği Yazanlarda "set" konusu izlenecek ve Python 101,102 ve 103 sertifikaları alınacak.
###############################################

###############################################
# KEYFİ ÖDEV 2: (TAKİP EDİLMEYECEK - SORULAR YANITLANAMAYACAKTIR)
# Python scriptine konsoldan arguman vermek konusunu araştırınız ve bir örnek uygulama yapınız.
# İpucu: argparse-CLIs (command line interfaces)
###############################################