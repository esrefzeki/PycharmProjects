# -*- coding: utf-8 -*-
"""cltv_calisma.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y3_QL1X-I-F6qkSPkyEDIjo3Z6oLqg06
"""

import pandas as pd

df_ = pd.read_excel("/content/drive/MyDrive/online_retail_II.xlsx",sheet_name="Year 2010-2011")

from google.colab import drive
drive.mount('/content/drive')

df = df_.copy()
df.head()

# Invoice`ta C olanlari at
df = df[~df["Invoice"].str.contains("C", na=False)]

#Negatif alisveris sayilarini at
df = df[(df['Quantity'] > 0)]

#NA`leri drop et
df.dropna(inplace=True)

#Total Price (Toplam Fiyat) sütunu ekle
df["TotalPrice"] = df["Quantity"] * df["Price"]

# Her bir customer ID icin fatura sayısı,toplam işlem, toplam fiyat degerlerini ver
cltv_df = df.groupby('Customer ID').agg({'Invoice': lambda x: len(x),
                                         'Quantity': lambda x: x.sum(),
                                         'TotalPrice': lambda x: x.sum()})

## fatura sayısı,toplam işlem, toplam fiyat
cltv_df.columns = ['total_transaction', 'total_unit', 'total_price']

cltv_df.head()

##Calculate Average Order Value

# CLTV = (Customer_Value / Churn_Rate) x Profit_margin(kar marjı) -> (Müsteri yasam boyu degeri)
# Customer_Value = Average_Order_Value * Purchase_Frequency/churn_rate
# Average_Order_Value = Total_Revenue / Total_Number_of_Orders -> (Ortalama Siparis (sepet) degeri (Toplam gelir/ Toplam siparis ))
# Purchase_Frequency =  Total_Number_of_Orders / Total_Number_of_Customers -> (Alim Satis Sikligi)
# Churn_Rate = 1 - Repeat_Rate-> (Pasif kullaniciya dusme)
# Profit_margin -> (Firmaya maliyeti ve satis arasindaki fark/Net kar)
###CLTV= (((Total_Revenue(toplam gelir) / Total_Number_of_Orders(toplam sipariş sayısı)) *  (Total_Number_of_Orders / Total_Number_of_Customers))/(1 - Repeat_Rate)) X Profit_margin

cltv_df.shape[0] # Total_Number_of_Customers

cltv_df.head(3)

#Average_Order_Value = Total_Revenue / Total_Number_of_Orders
cltv_df['avg_order_value'] = cltv_df['total_price'] / cltv_df['total_transaction']

# Purchase_Frequency =  Total_Number_of_Orders / Total_Number_of_Customers
cltv_df["purchase_frequency"] = cltv_df['total_transaction'] / cltv_df.shape[0]

# Churn_Rate = 1 - Repeat_Rate
repeat_rate = cltv_df[cltv_df.total_transaction > 1].shape[0] / cltv_df.shape[0]
churn_rate = 1 - repeat_rate

#Kar marjı-Profit_margin 
cltv_df['profit_margin'] = cltv_df['total_price'] * 0.05

#Customer_Value()
cltv_df['CV'] = (cltv_df['avg_order_value'] * cltv_df["purchase_frequency"]) / churn_rate

# CLTV = (Customer_Value / Churn_Rate) x Profit_margin(kar marjı) -> (Müsteri yasam boyu degeri)
# Customer_Value = Average_Order_Value * Purchase_Frequency/churn_rate
# Average_Order_Value = Total_Revenue / Total_Number_of_Orders -> (Ortalama Siparis (sepet) degeri (Toplam gelir/ Toplam siparis ))
# Purchase_Frequency =  Total_Number_of_Orders / Total_Number_of_Customers -> (Alim Satis Sikligi)
# Churn_Rate = 1 - Repeat_Rate-> (Pasif kullaniciya dusme)
# Profit_margin -> (Firmaya maliyeti ve satis arasindaki fark/Net kar)
###CLTV= (((Total_Revenue(toplam gelir) / Total_Number_of_Orders(toplam sipariş sayısı)) *  (Total_Number_of_Orders / Total_Number_of_Customers))/(1 - Repeat_Rate)) X Profit_margin

# CLTV = (Customer_Value / Churn_Rate) x Profit_margin(kar marjı)
cltv_df['CLTV'] = cltv_df['CV'] * cltv_df['profit_margin']

cltv_df.sort_values("CLTV", ascending=False)

#1-100 arası Transform
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(1, 100))
scaler.fit(cltv_df[["CLTV"]])
cltv_df["SCALED_CLTV"] = scaler.transform(cltv_df[["CLTV"]])

cltv_df.sort_values("CLTV", ascending=False)

cltv_df[["total_transaction", "total_unit", "total_price", "CLTV", "SCALED_CLTV"]].sort_values(by="SCALED_CLTV",
                                                                                               ascending=False).head()

cltv_df.sort_values("total_price", ascending=False)

#Segmentlere ayırma
cltv_df["segment"] = pd.qcut(cltv_df["SCALED_CLTV"], 4, labels=["D", "C", "B", "A"])

cltv_df[["segment", "total_transaction", "total_unit", "total_price", "CLTV", "SCALED_CLTV"]].sort_values(
    by="SCALED_CLTV",
    ascending=False).head()

cltv_df.groupby("segment")[["total_transaction", "total_unit", "total_price", "CLTV", "SCALED_CLTV"]].agg(
    {"count", "mean", "sum"})

# Total Transaction:Toplam Fatura Sayisi 
# Total Unit: Toplam Islem
# Total Price: Toplam Fiyat
# CLTV: Customer Lifetime Value (Müsteri Yasam Boyu Degeri)
# Scaled CLTV: Standardlastirilmis CLTV degerleri (1-100 skalasinda)