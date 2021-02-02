# Created and coded by Esref Zeki PARLAK

"""
PROJE 2 / Üçüncü Hafta
----------------------------
RFM MÜŞTERİ SEGMENTASYONU PROJESİ
----------------------------
Proje detayları ve firma istekleri burada yer almaktadır:
https://drive.google.com/file/d/1PyzF5oibzfYVFHOAfPFhgWRjITtDYeDX/view?usp=sharing

İŞ PROBLEMİ - AMAÇ:

Bir e-ticaret şirketi müşterilerini segmentlere ayırıp bu segmentlere göre
pazarlama stratejileri belirlemek istiyor.

İş problemine yönelik olarak müşterilerin davranışlarının tanımlanması ve
bu davranışlardaki öbeklenmelere göre gruplar oluşturulmak istenmekte.

İpucu:
Ortak davranışlar sergileyenler aynı gruplarda yer alacak ve bu gruplara özel
satış ve pazarlama teknikleri geliştirilmesinde geri bildirimler yapılacak.

VERİ SETİ HİKAYESİ / DETAYLAR::

Online Retail II isimli veri seti İngiltere merkezli online bir satış mağazasının
01/12/2009 - 09/12/2011 tarihleri arasındaki satışlarını içeriyor.
Bu şirketin ürün kataloğunda hediyelik eşyalar yer alıyor. Promosyon ürünleri olarak da düşünülebilir.
Çoğu müşterisinin toptancı olduğu bilgisi de mevcut.

- InvoiceNo: Fatura numarası. Her işleme yani faturaya ait eşsiz numara.
Eğer bu kod C ile başlıyorsa işlemin iptal edildiğini ifade eder.
- StockCode: Ürün kodu. Her bir ürün için eşsiz numara. Description: Ürün ismi
- Quantity: Ürün adedi. Faturalardaki ürünlerden kaçar tane satıldığını ifade etmektedir.
- InvoiceDate: Fatura tarihi ve zamanı.
- UnitPrice: Ürün fiyatı (Sterlin cinsinden)
- CustomerID: Eşsiz müşteri numarası Country: Ülke ismi. Müşterinin yaşadığı ülke.

"""

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

dfc = pd.read_excel('/Users/esrefzekiparlak/PycharmProjects/dsmlbc4/online_retail.xlsx')
df = dfc.copy()

def check_df(dataframe):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(3))
    print("##################### Tail #####################")
    print(dataframe.tail(3))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)

df.dropna(how='any', inplace=True)
df.isnull().sum()

df.head()

# Eşsiz ürün sayısı nedir?
df["Description"].nunique()
# SONUÇ: 3896

# Hangi üründen kaç tane var?
df["Description"].value_counts().head() # Değerleri value_counts ile teker teker sayar ve satır adı karşılığını verir

# En çok sipariş edilen ürün hangisi?
df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()

# Toplam kaç fatura kesilmiştir?
df["InvoiceNo"].nunique()

# Fatura başına ortalama kaç para kazanılmıştır?
df["InvoiceNo"].str.isnumeric()
df["InvoiceNo"].head(30)
df["InvoiceNo"].tail(30)
df = df[~df["InvoiceNo"].str.contains]

df.groupby("InvoiceNo").agg({"UnitPrice": "sum"}).head()

