# Created and coded by Esref Zeki PARLAK

"""
PROJE 1 / İkinci Hafta
----------------------------
LEVEL BASED PERSONA PROJESİ
----------------------------
Proje detayları ve firma istekleri burada yer almaktadır:
https://drive.google.com/file/d/1uZlVy2FHfV0FdqIbJ4LjiT8hiC7IOnwG/view?usp=sharing

İŞ PROBLEMİ - AMAÇ:

Tekil olarak var olan müşterilerin bazı özelliklerini kullanarak yeni müşteri
tanımlamaları yapmak, müşterileri "price" değişkenine göre segmentlere ayırmak ve yeni
gelecek bir müşterinin hangi segmente ait olabileceğini belirlemeye çalışmak.


DETAYLAR:

Müşterilerin özelliklerini ve işlem bilgilerini gösteren iki farklı
tablo mevcuttur.

users.csv tablosu müşterilerin karakteristik özelliklerini gösterirken,
purchases.csv tablosu müşterilerin satın alma bilgilerini barındırmaktadır.

Her bir kullanıcının kendisine özel (unique) bir müşteri numarası (uid) bulunmaktadır.
Her iki tabloyu birleştirme işlemi (uid) numarası ile yapılabilmektedir.
"""

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)

users = pd.read_csv('users.csv')
purchases = pd.read_csv('purchases.csv')

users.head() # users.head() ile hem sütunları hem de içeriği gözlemliyoruz.
users.columns # Sadece sütun bilgilerine eşirmek istediğimizde kullanırız.

# users.head() SONUÇ:
#         uid              reg_date device gender country  age
# 0  54030035  2017-06-29T00:00:00Z    and      M     USA   19
# 1  72574201  2018-03-05T00:00:00Z    iOS      F     TUR   22
# 2  64187558  2016-02-07T00:00:00Z    iOS      M     USA   16
# 3  92513925  2017-05-25T00:00:00Z    and      M     BRA   41
# 4  99231338  2017-03-26T00:00:00Z    iOS      M     FRA   59

purchases.head()
purchases.columns
# SONUÇ:
#          date       uid  price
# 0  2017-07-10  41195147    499
# 1  2017-07-15  41195147    499
# 2  2017-11-12  41195147    599
# 3  2017-09-26  91591874    299
# 4  2017-12-01  91591874    599

##################################################
# İki Farklı Veri Dosyasını Birleştirme İşlemi:
##################################################

# 1. users ve purchases veri setlerini okutunuz ve veri setlerini "uid" değişkenine göre inner join ile merge ediniz.

df = users.merge(purchases, how='inner', on='uid') # Detaylı bilgi: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
# AÇIKLAMA: Merge işleminde sol kısımda yer alan yani users.merge kısmında hangi users yazan yere neyi tanımlarsak
# onun tablosuna göre sıralama işlemini gerçekleştirir ve içeride merge edilen diğer veri birleştirme işleminden sonra
# users kısmının tablosuna eklenir. Burada kullanıcı uid baz alınarak birleştirme işlemi gerçekleştirildi.
df.head()

# SONUÇ:
#         uid              reg_date device gender country  age        date  \
# 0  92513925  2017-05-25T00:00:00Z    and      M     BRA   41  2017-10-20
# 1  92513925  2017-05-25T00:00:00Z    and      M     BRA   41  2017-05-29
# 2  92513925  2017-05-25T00:00:00Z    and      M     BRA   41  2017-08-23
# 3  92513925  2017-05-25T00:00:00Z    and      M     BRA   41  2018-03-26
# 4  16377492  2016-10-16T00:00:00Z    and      M     BRA   20  2018-03-17
#    price
# 0    499
# 1    299
# 2    599
# 3    299
# 4    199



# 2. country, device, gender, age kırılımında toplam kazançlar nedir?

# Elde edilmesi gereken çıktı:
#                            price
# country device gender age
# BRA     and    F      15   33824
#                       16   31619
#                       17   20352
#                       18   20047
#                       19   21352
#                       20   22640

df.groupby(["country", "device", "gender", "age"]).agg({"price": "sum"}).head()

# 3. Çıktıyı daha iyi görebilmek için kod'a sort_values metodunu azalan olacak şekilde price'a göre uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

# Elde edilmesi gereken çıktı (agg_df.head()):

#                            price
# country device gender age
# USA     and    M      15   61550
# BRA     and    M      19   45392
# DEU     iOS    F      16   41602
# USA     and    F      17   40004
#                M      23   39802

agg_df = df.groupby(["country", "device", "gender", "age"]).agg({"price": "sum"}).sort_values("price", ascending=False).head()
# Alternatif - 2: agg_df.sort_values("price", ascending=False).head()


# 4. agg_df'in index'lerini değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan price dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.

agg_df.reset_index(inplace=True)
agg_df.values



# 5. age değişkenini kategorik değişkene çeviriniz ve agg_df'e "age_cat" ismiyle ekleyiniz.
# Aralıkları istediğiniz şekilde çevirebilirsiniz fakat ikna edici olmalı.

# Elde edilmesi gereken çıktı:

#   country device gender  age  price age_cat
# 0     USA    and      M   15  61550    0_18
# 1     BRA    and      M   19  45392    0_18
# 2     DEU    iOS      F   16  41602    0_18
# 3     USA    and      F   17  40004    0_18
# 4     USA    and      M   23  39802   19_23

agg_df["age_cat"] = pd.cut(agg_df["age"],
                           bins=[0, 18, 23, 30, 40, 75],
                           labels=['0_18', '19_23', '24_30', '31_40', '41_75'])

agg_df.drop(['age'], axis=1)

agg_df

# 6. Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Önceki soruda elde ettiğiniz çıktıya göre veri setinde yer alan kategorik kırılımları
# müşteri grupları olarak düşününüz ve bu grupları birleştirerek yeni müşterileri tanımlayınız.

# Örneğin:
# USA_AND_M_0_18
# USA_AND_F_19_23
# BRA_AND_M_0_18


# Elde edilmesi gereken çıktı:

#   customers_level_based  price
# 0        USA_AND_M_0_18  61550
# 1        BRA_AND_M_0_18  45392
# 2        DEU_IOS_F_0_18  41602
# 3        USA_AND_F_0_18  40004
# 4       USA_AND_M_19_23  39802

agg_df["customer_level_based"] = [str(v[0] + "_" + v[1] + "_" + v[2] + "_" + v[5]).upper() for v in agg_df.values]


# 7. Yeni müşterileri price'a göre segmentlere ayırınız, "segment" isimlendirmesi ile agg_df'e ekleyiniz.
# Segmentleri betimleyiniz.


# "customers_level_based" değişkeni artık yeni müşteri tanımımız.
# Örneğin "USA_AND_M_0_18". ABD-ANDROID-MALE-0-18 sınıfı bizim için bir müşteri sınıfını temsil eden tek bir müşteridir.
# Bu yeni müşterileri price'a göre gruplara ayırınız.

# İpucu: Yeni müşterileri (customers_level_based) basitçe 4 gruba ayırınız (qcut fonksiyonu ile)
# ve A,B,C,D olarak isimlendiriniz. Bu grupları yeni veri setine ekleyiniz.

# Kod: pd.qcut(agg_df["price"], 4, labels=["D", "C", "B", "A"])


# Elde edilmesi gereken çıktı:

#   customers_level_based  price segment
# 0        USA_AND_M_0_18  61550       A
# 1        BRA_AND_M_0_18  45392       A
# 2        DEU_IOS_F_0_18  41602       A
# 3        USA_AND_F_0_18  40004       A
# 4       USA_AND_M_19_23  39802       A
# 5        USA_IOS_M_0_18  39402       A

agg_df["segment"] = pd.qcut(agg_df["price"], 4, labels=["A", "B", "C", "D"])
agg_df_new = agg_df[["customer_level_based", "price", "segment"]]

agg_df_new.head()

# Segmentleri betimleyiniz çıktısı:

#             price
# segment
# D        1335.096
# C        3675.505
# B        7447.812
# A       20080.150

agg_df_new.groupby('segment').agg({'price': 'mean'}).sort_values("price", ascending=False).head()

agg_df_new.reset_index()
# 8. 42 yaşında IOS kullanan bir Türk kadını hangi segmenttedir?
# agg_df tablosuna göre bu kişinin segmentini (grubunu) ifade ediniz.
# İpucu: new_user = "TUR_IOS_F_41_75"

# Çıktı:
#     customers_level_based  price segment
# 377       TUR_IOS_F_41_75   1596       D

#new_group = agg_df[agg_df["customer_level_based"]=="TUR_IOS_F_41_75"]

new_group = "TUR_IOS_F_41_75"
agg_df_new[agg_df_new['customers_level_based'] == new_user]



#********************
# KENDİME NOTLAR:
#********************

# Herhangi bir değer içerisinde farklı değişkenler içeriyor dahi olsa
# aşağıdaki gibi tüm farklı değişkenlere göre saydırma yapabiliriz:
users["gender"].value_counts()