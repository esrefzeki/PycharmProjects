import pandas as pd
import numpy as np
import datetime as dt

pd.set_option('display.max_columns', None) # Burada çıktıların tam açılımının yazılması gerektiğini ifade ediyoruz
# pd.set_option('display.max_rows', 20)

df = pd.read_excel("online_retail.xlsx")

# df = pd.read_excel("online_retail.xlsx",
#                    sheet_name="Year 2010-2011")
# Excel dosyasını okutuyoruz ve başlığını sheet_name olarak atıyoruz

dfc = df.copy() # We save the backup of our df file as a dfc backup

df.head()

df.isnull().sum() # We are looking at the sum of the data that is NaN

# Eşsiz urun sayisi nedir?
df["Description"].nunique()

# How many of the products are there?
df["Description"].value_counts().head()

# How many independent different customers are there from which country?
df.groupby("Country")["CustomerID"].nunique() # Alternative 1
df.groupby("Country").agg("CustomerID").nunique() # Alternative 2 ### NASIL SORT EDECEĞİZ?!!!

# Which is the most ordered product?
df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()


df.groupby(["Description"]).count()[{"Quantity": "sum"}].head() # Her bir verinin sağdaki verisi kadar saydırma işlemi

# How many invoices have been issued?
df["InvoiceNo"].nunique()

# fatura basina ortalama kac para kazanilmistir? ,
# (iki değişkeni çarparak yeni bir değişken oluşturmak gerekmektedir)
# iadeleri çıkararak yeniden df'i oluşturalım
df = df[~df["InvoiceNo"].str.contains("C", na=False)] ###ANLAŞILMADI!!!
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

df.sort_values("TotalPrice", ascending=False)

# en pahalı ürünler hangileri?
df.sort_values("UnitPrice", ascending=False).head()
df.groupby("Description").agg("UnitPrice").sort_values("UnitPrice", ascending=False).head()

# hangi ulkeden kac siparis geldi?
df["Country"].value_counts() # NEYE GÖRE SIRALIYOR? SİPARİŞ İLE BİLGİ GİRİLMEDİ?!!!


# hangi ulke ne kadar kazandırdı?
df.group("Country").agg({"TotalPrice": "sum"}).sort_values("TotalPrice", ascending=False).head()