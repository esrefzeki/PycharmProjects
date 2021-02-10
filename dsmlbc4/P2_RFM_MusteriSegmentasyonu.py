# Created and coded by Esref Zeki PARLAK

"""
PROJE 2 / İkinci Hafta
----------------------------
CUSTOMER SEGMENTATION BY USING RFM PROJESİ
----------------------------
Proje detayları ve firma istekleri burada yer almaktadır:
https://drive.google.com/file/d/1PyzF5oibzfYVFHOAfPFhgWRjITtDYeDX/view?usp=sharing

İŞ PROBLEMİ - AMAÇ:

Bir e-ticaret şirketi müşterilerini segmentlere ayırıp bu
segmentlere göre pazarlama stratejileri belirlemek istiyor.

İş problemine yönelik olarak müşterilerin davranışlarının tanımlanması ve
bu davranışlardaki öbeklenmelere göre gruplar oluşturulmak istenmekte.

İpucu:
Ortak davranışlar sergileyenler aynı gruplarda yer
alacak ve bu gruplara özel satış ve pazarlama
teknikleri geliştirilmesinde geri bildirimler yapılacak.

DETAYLAR:

Online Retail II isimli veri seti İngiltere merkezli online bir satış mağazasının
01/12/2009 - 09/12/2011 tarihleri arasındaki satışlarını içeriyor.

Bu şirketin ürün kataloğunda hediyelik eşyalar yer alıyor. Promosyon ürünleri olarak
da düşünülebilir.

Çoğu müşterisinin toptancı olduğu bilgisi de mevcut.

InvoiceNo: Fatura numarası. Her işleme yani faturaya ait eşsiz
numara. Eğer bu kod C ile başlıyorsa işlemin iptal edildiğini
ifade eder.
StockCode: Ürün kodu. Her bir ürün için eşsiz numara.
Description: Ürün ismi
Quantity: Ürün adedi. Faturalardaki ürünlerden kaçar tane
satıldığını ifade etmektedir.
InvoiceDate: Fatura tarihi ve zamanı.
UnitPrice: Ürün fiyatı (Sterlin cinsinden)
CustomerID: Eşsiz müşteri numarası
Country: Ülke ismi. Müşterinin yaşadığı ülke.

"""

import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)  # Burada çıktıların tam açılımının yazılması gerektiğini ifade ediyoruz.
# pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df = pd.read_csv("online_retail_II.csv")

# df = pd.read_csv("online_retail_II.csv",
#                  sheet_name="Year 2010-2011)

# Excel dosyasını okutuyoruz ve başlığını sheet_name olarak atıyoruz.


dfc = df.copy()  # Burada df veri setimizin yedeğini kopyalayıp tutuyoruz, böylece bir sorun yaşandığında sıfırdan işlem yapabiliriz.

df.head()

df.isnull().sum()  # NaN olan yani bilinmeyen değerlerin toplamına bakıyoruz.

# Eşsiz urun sayisi nedir?
df["Description"].nunique()  # Ürün isim başlıklarının her biri benzersiz bir ürün olduğu düşünülürse nunique ile benzersiz şekilde saydırırız

# Hangi üründen kaçar tane var?
df["Description"].value_counts().head()  # Value_counts ile her bir ürün başlığından kaç adet ürün olduğunu buluruz
df["Customer ID"].unique()

# How many independent different customers are there from which country?
df.groupby("Country")["Customer ID"].nunique()  # Alternative 1
df.groupby("Country").agg("Customer ID").nunique()  # Alternative 2

# >>>>> SORU-1:Hangi ülkeden kaç müşteri olduğunu nasıl sort edeceğiz?


# En çok sipariş edilen ürün hangisi?
df.groupby(["Description"]).count()[{"Quantity": "sum"}].sort_values("Quantity", ascending=False).head()
# df.loc[df["StockCode"] == 84077, "Description"] # Stok kodu 84077 olan ürünün adını sorguluyoruz.


# Yukarıdaki çıktıyı nasıl sıralarız?
df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()

# Toplam kaç fatura kesilmiştir?
df["Invoice"].nunique()

# Her bir kesilen fatura başına ortalama kaç para kazanılmıştır?
# (iki değişkeni çarparak yeni bir değişken oluşturmak gerekmektedir)
# iadeleri çıkararak yeniden df'i oluşturalım

df = df[~df["Invoice"].str.contains("C", na=False)]  # ~ Tilda işareti mevcut işlemin tersini almamızı sağlar
df["TotalPrice"] = df["Quantity"] * df["Price"]
df.sort_values("TotalPrice", ascending=False)
ax = df[df.totalprice == 7]
ax
# >>>>> SORU-1: NEDEN 'SeriesGroupBy' object has no attribute 'sort_values' HATASI ALIYORUZ?
# >>>>> SORU-2: InvoiceNo'ları bir arada derleyip toplam fiyatına göre sıralamak istediğimizde ne yapıyoruz?
# df.groupby("InvoiceNo").agg("TotalPrice").sort_values("UnitPrice", ascending=False).head()
# *********************


# En pahalı ürünler hangileri?
df.sort_values("Price", ascending=False).head()
# >>>>> SORU-1: Aşağıda pahalı kod satırında pahalı en pahalı ürün ile ücretini birlikte getirmek istiyorum fakat hata alıyorum.
# df.groupby("Description").agg("UnitPrice").sort_values("UnitPrice", ascending=False).head()
# >>>>> SORU-2: AMAZON FEE bir ürün değil. Bu sıralamada yanlışlık var gibi gözüküyor. Ayrıca


# Hangi ülkeden kaç sipariş geldi?
df["Country"].value_counts()
# >>>>> SORU-1: NEYE GÖRE SIRALIYOR? SİPARİŞ İLE BİLGİ GİRİLMEDİ? Bu CustomerID'ye göre mi yoksa InvoiceNo'ya göre mi geldi?


# Hangi ülke ne kadar kazandırdı?
df.groupby("Country").agg({"TotalPrice": "sum"}).sort_values("TotalPrice", ascending=False).head()

df.sort_values("TotalPrice", ascending=False).head()

###############################################################
# Data Preparation
###############################################################

# Bu bölümde veriyi hazırlama amaçlı Na değerlerinin toplamını analiz edip bu Na'ları gözlemden çıkartarak
# verinin içerisine kaydediyoruz ve akabinde df.describe ile detaylı gözlem yapmak üzere
# Na'dan arındırılmış veriler üzerinde aykırı değer incelemesini yapıyoruz.

df.isnull().sum()
df.dropna(inplace=True)

df.describe([0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]).T

###############################################################
# Calculating RFM Metrics
###############################################################

# Recency, Frequency, Monetary

# Recency (yenilik): Müşterinin son satın almasından bugüne kadar geçen süre
# Diğer bir ifadesiyle “Müşterinin son temasından bugüne kadar geçen süre” dir.


# Bugünün tarihi - Son satın alma

df["InvoiceDate"].max() # En son yapılan alışveriş yapılan tarih ve/veya saati görmek için InvoiceDate içeriğindeki max değeri çağırıyoruz.

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) # Burada InvoiceDate object olarak kayıtlıydı,
# onu zaman dilimine çevirmek için pd.to_datetime kullandık ve zaman tipine çevirdik.

today_date = dt.datetime(2010, 12, 11) # today_date atayarak mevcut bir gün belirleyerek o güne göre göre işlem yapmayı amaçladık

# Aşağıda rfm adında bir değişken tanımladık ve Customer ID'ye göre toplama işlemi gerçekleştirdik.
# InvoiceDate, Invoice ve TotalPrice üzerinden lambda ile çeşitli işlemler yaparak atamalar yaptık
# Böylece amacımıza uygun hale getirerek veriyi kullanmayı amaçlıyoruz:
rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                     'Invoice': lambda num: len(num),
                                     'TotalPrice': lambda TotalPrice: TotalPrice.sum()})

# RFM puanlaması için yeni kolonlar tanımladık ve bunlara göre bir skor oluşturmayı amaçlıyoruz:
rfm.columns = ['Recency', 'Frequency', 'Monetary']


###############################################################
# Calculating RFM Scores
###############################################################

# Recency

# Aşağıda yine rfm içerisinde yeni kolonlar oluşturarak bunların qcut ile
# önceden oluşturmuş olduğumuz skor kolonlarına göre bölümlere ayırıyoruz.
# Hangi kolonu, kaç bölüme ve neye göre belirleyeceğimizi belirtiyoruz:
rfm["RecencyScore"] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])

rfm["FrequencyScore"] = pd.qcut(rfm['Frequency'], 5, labels=[1, 2, 3, 4, 5])

rfm["MonetaryScore"] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

# Sonuç olarak RFM_SCORE oluşturup string formatında bir atama yapıyoruz.
# Böylece işlem toplama işlemine girmeden string değer olarak yan yana geliyor:
rfm["RFM_SCORE"] = (rfm['RecencyScore'].astype(str) +
                    rfm['FrequencyScore'].astype(str) +
                    rfm['MonetaryScore'].astype(str))

# rfm kolonu içerisinde rfm kolonu olan RFM_SCORE içerisinden 555 puanına sahip olan
# değerleri bir araya getirerek head kısmını çağırıyoruz:
rfm[rfm["RFM_SCORE"] == "555"].head()

# Aynı şekilde 111 puanına sahip olanları çağırıyoruz:
rfm[rfm["RFM_SCORE"] == "111"]



###############################################################
# Naming & Analysing RFM Segments
###############################################################

# RFM isimlendirmesi
seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At_Risk',
    r'[1-2]5': 'Cant_Loose',
    r'3[1-2]': 'About_to_Sleep',
    r'33': 'Need_Attention',
    r'[3-4][4-5]': 'Loyal_Customers',
    r'41': 'Promising',
    r'51': 'New_Customers',
    r'[4-5][2-3]': 'Potential_Loyalists',
    r'5[4-5]': 'Champions'
}

# YUKARIDA seg_map değişkeni oluşturarak r ile sınıf ataması gerçekleştirdik.
# Sınıf atamalarını belirli değişkenlere göre belirledik.
# String olarak atama yaptığımızı burada önemle altını çizmek gerekiyor.

rfm

# rfm'de Segment adında bir kolon oluşturuyoruz ve içerisine string typeta RecencyScore ile
# FrequencyScore çıktılarını yan yana getiriyoruz.
rfm['Segment'] = rfm['RecencyScore'].astype(str) + rfm['FrequencyScore'].astype(str)

# Segment kolonunu replace ile segmap içerisinde regex uyguluyoruz ve oradaki verilere göre sınıflandırıyoruz.
rfm['Segment'] = rfm['Segment'].replace(seg_map, regex=True)

# df.head()

df[["Customer ID"]].nunique()

# Yine aşağıdaki kod parçasında çeşitli kolonlara göre groupby işlemini segment bazında sınıflayıp
# her kolona göre ortalamayı ve sayısını alıyoruz.
# Böylece ayırdığımız segmentasyona göre bir derleme yapıyoruz.
rfm[["Segment", "Recency", "Frequency", "Monetary"]].groupby("Segment").agg(["mean", "count"])

# Aşağıda ise Need_Attention sınıfında yer alanların head ve indexine bakıyoruz:
rfm[rfm["Segment"] == "Need_Attention"].head()
rfm[rfm["Segment"] == "Need_Attention"].index

new_df = pd.DataFrame()

new_df["Need_Attention"] = rfm[rfm["Segment"] == "Need_Attention"].index

new_df.to_csv("Need_Attention.csv")