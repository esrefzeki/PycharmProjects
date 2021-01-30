#############################################
# ZORUNLU ODEV: Aşağıdaki soruları yanıtlayınız.
#############################################

# 1. users ve purchases veri setlerini okutunuz ve veri setlerini "uid" değişkenine göre inner join ile merge ediniz.
# 2. Kaç unique müşteri vardır?
# 3. Kaç unique fiyatlandırma var?
# 4. Hangi fiyattan kaçar tane satılmış?
# 5. Hangi ülkeden kaçar tane satış olmuş?
# 6. Ülkelere göre satışlardan toplam ne kadar kazanılmış?
# 7. Device türlerine göre göre satış sayıları nedir?
# 8. ülkelere göre fiyat ortalamaları nedir?
# 9. Cihazlara göre fiyat ortalamaları nedir?
# 10. Ülke-Cihaz kırılımında fiyat ortalamaları nedir?

#############################################

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

users = pd.read_csv("users.csv")
users.head()

purchases = pd.read_csv("purchases.csv")
purchases.head()


# SORU 1: Users ve purchases veri setlerini okutunuz ve veri setlerini "uid" değişkenine göre inner join ile merge ediniz.

# Eklendiğini teyit etmek için kontrol edilir:
purchases.shape # 3
users.shape # 6

# Burada users ile purchases verileri içerisinde yer alan ortak uid'lere göre purchases dosyasının içerisindeki
# verileri users uid'sindeki verilere karşılık gelecek şekilde merge ettik:
df = users.merge(purchases, how='inner', on='uid')

df.head()
df.shape # 8 # Verilerin birleştiğini teyit ediyoruz

# SORU 2: Kaç unique müşteri vardır?

df['uid'].nunique() #1322

# 3. Kaç unique fiyatlandırma var?

df['price'].nunique() # 6

# 4. Hangi fiyattan kaçar tane satılmış?

df.groupby('price').agg({'price': ['count']})

# SONUÇ:

#       price
#       count
# price
# 99      357
# 199    1840
# 299    2347
# 499    2242
# 599    1848
# 899     372

# 5. Hangi ülkeden kaçar tane satış olmuş?

df.groupby('country').agg({'country': ['count']})

# SONUÇ:

#         country
#           count
# country
# BRA        2694
# CAN         399
# DEU         915
# FRA         544
# TUR         804
# USA        3650

# 6. Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby('country').agg({'price': ['sum']})

# SONUÇ:

#            price
#              sum
# country
# BRA      1104106
# CAN       158901
# DEU       374285
# FRA       218556
# TUR       333996
# USA      1473550

# 7. Device türlerine göre göre satış sayıları nedir?

df.groupby('device').agg({'device': ['count']})

# SONUÇ:

#        device
#         count
# device
# and      5345
# iOS      3661

# 8. ülkelere göre fiyat ortalamaları nedir?

df.groupby('country').agg({'price': ['mean']})

# SONUÇ:

#               price
#                mean
# country
# BRA      409.838901
# CAN      398.248120
# DEU      409.054645
# FRA      401.757353
# TUR      415.417910
# USA      403.712329

# 9. Cihazlara göre fiyat ortalamaları nedir?

df.groupby('device').agg({'price': ['mean']})

# SONUÇ:

#              price
#               mean
# device
# and     408.111319
# iOS     404.818082

# 10. Ülke-Cihaz kırılımında fiyat ortalamaları nedir?

df.groupby(['country', 'device']).agg({'price': ['mean']})

#                      price
#                       mean
# country device
# BRA     and     412.985594
#         iOS     404.739300
# CAN     and     406.826087
#         iOS     386.573964
# DEU     and     402.474903
#         iOS     417.639798
# FRA     and     418.377163
#         iOS     382.921569
# TUR     and     433.913793
#         iOS     390.176471
# USA     and     399.000000
#         iOS     410.684783
