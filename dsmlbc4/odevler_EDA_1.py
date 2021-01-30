
#############################################
# ÖDEVLER
#############################################

#############################################
# ZORUNLU ODEV: Aşağıdaki soruları yanıtlayınız.
#############################################
import pandas as pd

users = pd.read_csv('./week_2/datasets/users.csv')
purchases = pd.read_csv('./week_2/datasets/purchases.csv')
users.shape, purchases.shape

# 1. users ve purchases veri setlerini okutunuz ve veri setlerini "uid" değişkenine
# göre inner join ile merge ediniz.
df = users.merge(purchases, how='inner', on='uid')
df.shape
df.head()


# 2. Kaç unique müşteri vardır?
df['uid'].nunique()
# 1322


# 3. Kaç unique fiyatlandırma var?
df['price'].nunique()
# 6


# 4. Hangi fiyattan kaçar tane satılmış?
df.groupby('price').agg({'price':['count']})


# 5. Hangi ülkeden kaçar tane satış olmuş?
df.groupby('country').agg({'country':['count']})


# 6. Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby('country').agg({'price':['sum']})


# 7. Device türlerine göre göre satış sayıları nedir?
df.groupby('device').agg({'device':['count']})
# and  5345
# iOS  3661


# 8. ülkelere göre fiyat ortalamaları nedir?
df.groupby('country').agg({'price':['mean']})


    # make sure that mean discard 'NaN' entries
df.groupby('country').agg({'price':['mean']}).loc['TUR']  # ---> 415.41791
df.groupby('country').agg({'price':['sum']}).loc['TUR']   # ---> 333996.0 total payment
df.groupby('country').agg({'price':['sum']}).loc['TUR']  / len(df[(df['country']=='TUR') & (df['price'].notnull())])
                                                            # --->> 415.41791 well done!, the 'NaN' values are discarded.
    # df[(df['country']=='TUR')]['price'].count()
    # len(df[(df['country']=='TUR') & (df['price'].notnull())])


# 9. Cihazlara göre fiyat ortalamaları nedir?
df.groupby('device').agg({'price':['mean']})
# and : 408.111319
# iOS : 404.818082


# 10. Ülke-Cihaz kırılımında fiyat ortalamaları nedir?
df.groupby(['country', 'device']).agg({'price':['mean']})

