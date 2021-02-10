import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import itertools
import statsmodels.stats.api as sms


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


df = pd.read_csv(r"C:\Users\yilma\PycharmProjects\DSMLBC-4\datasets\pricing.csv", sep=";")

df.head(10)
df.shape
df.isnull().sum()

#category id bir kategorik degisken oldugu icin object tipine donusturuldu..
df["category_id"].value_counts()
df["category_id"].unique()
df["category_id"] = df["category_id"].astype("O")

df.describe().T
df.groupby('category_id').agg(["mean", "median","count"])
def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.02)
    quartile3 = dataframe[variable].quantile(0.85)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

replace_with_thresholds(df,"price")
df.describe().T
df.describe([0.01, 0.05, 0.15, 0.25, 0.5, 0.75, 0.95,0.96,0.97,0.98, 0.99]).T

df.head()
df.groupby('category_id').agg(["mean", "median","count","max","std"])


sns.catplot(x='category_id', y='price',data=df, kind="box")
plt.show()





#######################################################################################################
#Soru 1 - Item'in fiyatı kategorilere göre farklılık göstermekte midir? İstatistiki olarak ifade ediniz.
#######################################################################################################
#Normal Dağılım
#H0: Normal Dağılım sağlanmaktadır.
#H1: Normal Dağılım sağlanmamaktadır.


import itertools
group_list = []
for i in itertools.combinations(df["category_id"].unique(), 2):
    group_list.append(i)
group_list


# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dagilim varsayimi sağlanmamaktadır.
#p<0.05 -> H0 red. Normal dagilmamaktadir.
#p>0.05 ->  H0 reddedilemez. Normal dagilmaktadir.

# H0: anlamli farklilik yoktur.
# H1: anlamli farklilik vardir.
stats.shapiro(group_list)

def ab_test(group_a,group_b):
    grb_a = df.loc[df["category_id"] == group_a,"price"]
    grb_b = df.loc[df["category_id"] == group_b, "price"]
    norm_a = stats.shapiro(grb_a)[1] >= 0.05
    norm_b = stats.shapiro(grb_b)[1] >= 0.05

    if norm_a and norm_b:
        var_h = stats.levene(grb_a,grb_b)[1] >= 0.05
        if var_h:
            t_test1= stats.ttest_ind(grb_a,grb_b,equal_var=True)[1]>=0.05
            if t_test1:
                print(f"{group_a} ve {group_b} ortalamaları arasında istatistiksel anlamlı farklılık yoktur")
            else:
                print(f"{group_a} ve {group_b} ortalamaları arasında istatistiksel anlamlı farklılık vardır")
        else:
            t_test2 = stats.ttest_ind(grb_a, grb_b, equal_var=False)[1] >= 0.05
            if t_test2:
                print(f"{group_a} ve {group_b} ortalamaları arasında istatistiksel anlamlı farklılık yoktur")
            else:
                print(f"{group_a} ve {group_b} ortalamaları arasında istatistiksel anlamlı farklılık vardır")
    else:
        t_test3 = stats.mannwhitneyu(grb_a, grb_b)[1] >= 0.05
        if t_test3:
            print(f"{group_a} ve {group_b} ortalamaları arasında istatistiksel anlamlı farklılık yoktur")
        else:
            print(f"{group_a} ve {group_b} ortalamaları arasında istatistiksel anlamlı farklılık vardır")


for groups in group_list:
    ab_test(groups[0],groups[1])

# item fiyati kategorilerin bir kismina  gore farklilik gosteriyor

###################################################################################
# SORU 2  İlk soruya bağlı olarak item'ın fiyatı ne olmalıdır? Nedenini açıklayınız?

####################################################################################
# 489756 ve 326584 için ayrı ayrı medyan degerleri fiyat olarak belirlenebilir
#489756'nin ve 326584 mean price'i genelden yuksek fakat median degeri genele yakin
df.groupby('category_id').agg(["mean", "median","count","max","std"])

df.loc[df["category_id"] == 489756, "price"].median()
# fiyat: 35.635784234

df.loc[df["category_id"] == 326584, "price"].median()
# fiyat: 31.7482419128


cat = [361254, 675201, 201436, 874521]
total_price= 0
for i in cat:
    total_price += df.loc[df['category_id'] == i, 'price'].mean()
price_ort = total_price/4
df["category_id"].value_counts()
#tum kategoriler icin icin price_avg (42.34) tutari kullanilabilir

######################################################################################################################
#SORU 3 Fiyat konusunda "hareket edebilir olmak" istenmektedir.
# Fiyat stratejisi için karar destek sistemi oluşturunuz.


######################################################################################################################
#belirleyici sinifin fiyatlarini bir araya getirelim
prices=[]
for category in cat:
    for i in df.loc[df["category_id"]== category,"price"]:
        prices.append(i)
sms.DescrStatsW(prices).tconfint_mean()
#fiyat araligi (41.751141105523956, 47.198110941285336) arasinda secilmelidir



############################################################################
#SORU 4 Olası fiyat değişiklikleri için item satın almalarını ve
#gelirlerini simüle ediniz.
############################################################################

#fiyat guven araliginin altinda olmasi durumunda elde edilecek gelir :
below_avg = df.loc[df['price'] <= 41, 'price'].mean()
below_no = df.loc[df['price'] <= 41, 'price'].count()
income_for_below = below_no * below_avg

#fiyat guven araliginin ustunde olmasi durumunda elde edilecek gelir:
above_avg = df.loc[df['price'] >= 32, 'price'].mean()
above_no = df.loc[df['price'] >= 32, 'price'].count()
income_for_above = above_avg * above_no
