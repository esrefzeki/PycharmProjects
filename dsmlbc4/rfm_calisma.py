# -*- coding: utf-8 -*-
"""RFM_Calisma.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J7fVRTMABVBAEKysKVZAvGidkHc-EtSd

görev 1
"""

import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_ = pd.read_excel("/content/drive/MyDrive/online_retail_II.xlsx",sheet_name="Year 2010-2011")

df = df_.copy()

df.isnull().sum()

# essiz urun sayisi nedir?
df["StockCode"].nunique()

# hangi urunden kacar tane var?
df["StockCode"].value_counts()

# en cok siparis edilen urun hangisi?
df.groupby("StockCode").agg({"Quantity": "sum"}).head()


# yukarıdaki çıktıyı nasil siralariz?
df.groupby("StockCode").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()

# toplam kac fatura kesilmiştir?
df["Invoice"].nunique()

# Na`lari silme
df.dropna(inplace=True)

# Fatura başına ortalama kaç para kazanılmıştır?
# (iki değişkeni çarparak yeni bir değişken oluşturmak gerekmektedir)
# iadeleri çıkararak yeniden df'i oluşturalım
# fonksiyon açıklaması tartışılacak.

df = df[~df["Invoice"].str.contains("C", na=False)]
df["TotalPrice"] = df["Quantity"] * df["Price"]

# en pahalı ürünler hangileri?
df.sort_values("Price", ascending=False).head()

# hangi ulkeden kac siparis geldi?
df["Country"].value_counts()

# hangi ulke ne kadar kazandırdı?
df.groupby("Country").agg({"TotalPrice": "sum"}).sort_values("TotalPrice", ascending=False).head()

# Data Preparation
###############################################################

df.isnull().sum()
#df.dropna(inplace=True)

df.describe([0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]).T

df["InvoiceDate"].max()

today_date = dt.datetime(2011, 12, 11)

df.head()

rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                     'Invoice': lambda num: num.nunique(),
                                     'TotalPrice': lambda TotalPrice: TotalPrice.sum()})

 #Len Na dahil hepsini sayiyor
 #Count Na haric hepsini sayiyor.
 #nunique tekillleri sayiyor.
 # 'Invoice': lambda num: len(num) : Kisi bazinda toplam fatura sayisi.Faturadaki her islem göz önüne alinir.
 # 'Invoice': lambda num: num.nunique(): Kisi bazinda tekil fatura sayisi. Her fatura bir islem kabul ediliyor.

rfm

rfm.columns = ['Recency', 'Frequency', 'Monetary']

rfm = rfm[(rfm["Monetary"]) > 0 & (rfm["Frequency"] > 0)]

rfm["RecencyScore"] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])


rfm["FrequencyScore"] = pd.qcut(rfm['Frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]) # 5`e bölerken arada kalirsa yukardaki gruba ata. 

rfm["MonetaryScore"] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])


rfm["RFM_SCORE"] = (rfm['RecencyScore'].astype(str) +
                    rfm['FrequencyScore'].astype(str) +
                    rfm['MonetaryScore'].astype(str))

rfm[rfm["RFM_SCORE"] == "555"].head()

rfm[rfm["RFM_SCORE"] == "111"]

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

seg_map

rfm

rfm['Segment'] = rfm['RecencyScore'].astype(str) + rfm['FrequencyScore'].astype(str)

rfm['Segment'] = rfm['Segment'].replace(seg_map, regex=True)
df[["Customer ID"]].nunique()
rfm[["Segment", "Recency", "Frequency", "Monetary"]].groupby("Segment").agg(["mean", "count"])

rfm[rfm["Segment"] == "Need_Attention"].head()
rfm[rfm["Segment"] == "Need_Attention"].index
rfm

new_df = pd.DataFrame()

new_df["Need_Attention"] = rfm[rfm["Segment"] == "Need_Attention"].index

new_df.head()



"""Görev 2 """



rfm[["Segment", "Recency", "Frequency", "Monetary"]].groupby("Segment").agg(["mean", "count"])

#Görev 3

new_df =rfm[rfm["Segment"].str.contains("Loyal_Customers", na=False)]
new_df

new_df.to_excel("Loyal_Customers.xlsx")