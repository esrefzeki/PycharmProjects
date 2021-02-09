import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import shapiro
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats.stats import pearsonr

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df = pd.read_csv("datasets/pricing.csv", sep=";")
data = df.copy()
data.info()
data.quantile([0, 0.05, 0.10, 0.25, 0.50, 0.75, 0.95, 0.97, 0.98, 0.99, 1]).T


def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.02)
    quartile3 = dataframe[variable].quantile(0.98)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit


def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    # dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit


replace_with_thresholds(data, "price")
data.quantile([0, 0.05, 0.10, 0.25, 0.50, 0.75, 0.95, 0.97, 0.98, 0.99, 1]).T

data.groupby("category_id").agg({"price": ["median", "count"]})

#  Normallik varsayımı

list = [201436, 326584, 361254, 489756, 675201, 874521]
for i in list:
    if shapiro(data.loc[df["category_id"] == i, "price"])[1] > 0.05:
        print("Normal dağılmaktadır")
    else:
        print("Normal dağılmamaktadır")

# Normal dağılmamaktadır
# Normal dağılmamaktadır
# Normal dağılmamaktadır
# Normal dağılmamaktadır
# Normal dağılmamaktadır
# Normal dağılmamaktadır

A = data.loc[df["category_id"] == 201436, "price"]
B = data.loc[df["category_id"] == 326584, "price"]
C = data.loc[df["category_id"] == 361254, "price"]
D = data.loc[df["category_id"] == 489756, "price"]
E = data.loc[df["category_id"] == 675201, "price"]
F = data.loc[df["category_id"] == 874521, "price"]

#                price
#                 mean count
# category_id
# 201436      36.17550    97
# 326584      38.69892   145
# 361254      38.99380   620
# 489756      53.69214  1705
# 675201      44.07083   131
# 874521      50.14933   750


#                price
#               median count
# category_id
# 201436      33.53468    97
# 326584      31.74824   145
# 361254      34.45919   620
# 489756      35.63578  1705
# 675201      33.83557   131
# 874521      34.40086   750

from scipy import stats

test_istatistigi, pvalue = stats.kruskal(A, B, C, D, E, F)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

# Output: Test İstatistiği = 189.0247, p-değeri = 0.0000
# Bu test sonucu bize anlamlı bir farklılığın olduğunu göstermektedir.


data.groupby("category_id").agg({"price": ["median"]}).median()
# Output: price  median   34.11821
std_data = data.groupby("category_id").agg({"price": ["median"]}).std()
std_data = 1.29124
# median için
data[data["price"] >= 34.11821-1.29124].count() * (34.11821-1.29124)
# 2361 kişi ile 77504.47617 getiri
data[data["price"] >= 34.11821].count() * 34.11821
# 2006 kişi ile 68441.12926 getiri


# Sonuç:
# Category idlere bakıldığında %99 lik ve üzeri seviyede outlier bulunmaktaydı ve onlar baskılandı.
# Değerlere bakıldığında normal dağılmadığı bulunmulştur.
# Category Id kırılımınlarında mean ve median değerline bakıldığında birbirlerine yakın olduğu görülmektedir.
# Kruskal testi sonucu bize anlamlı bir farklılığın olduğunu göstermektedir.
# Normal dağılmadığı için median değerlerinin median değerleri alınarak önderilecek fiyat belirlendi.
# Median için:
# 34.11821 fiyata almaya razı 2006 kişi bulunmaktadır ve geliri 68441.12926 tl olmaktadır
# Mediandan 1 standart sapmayı çıkardığımızda 2361 kişi ile 77504.47617 getiri olmaktadır.
# Fiyat median +1std -1std arasında belirlenebilir.