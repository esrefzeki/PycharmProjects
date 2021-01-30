#############################################
# EXPLORATORY DATA ANALYSIS USING PANDAS
#############################################

# Dersler
# Mentor Görüşmesi

# EKSTRALAR:

# Ödev atölyeleri
# Grupların kendi içinde kendi iradeleriyle açtığı çalışma grupları
# After party'ler
# Personal marketing için öneriler (kaggle, github, linkedin vs.)
# Ek dersler

# Rahatlatmalar
# Ek açıklamalar, pozisyon alma
# PyCharm ve fonksiyonel gidiş.


#############################################
# NUMPY
#############################################

import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Numerical Python
# Bilimsel hesaplamalar için kullanılır.
# Arrayler / çok boyutlu arrayler ve matrisler üzerinde yüksek performanslı çalışma imkanı sağlar.
# Temelleri 1995’te (matrix-sig, Guido Van Rossum) atılmış nihai olarak 2005 (Travis Oliphant) yılında hayata geçmiştir.
# Listelere benzerdir, farkı; verimli veri saklama ve vektörel operasyonlardır.

# https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference?module_item_id=10959918

# Why Numpy?
# Creating Numpy Arrays
# Attibutes of Numpy Arrays
# Reshaping
# Index Selection
# Slicing
# Fancy Index
# Conditions on Numpy
# Mathematical Operations
# Python Lists vs. Numpy Arrays


#############################################
# Why Numpy?
#############################################

# Python'da iki vektörün elemanlarının çarpımı
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

ab

# Aynı işlemin numpy ile yapılışı
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

#############################################
# Creating Numpy Arrays
#############################################

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))
np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))
np.random.randint(0, 10, (3, 3))

#############################################
# Attibutes of Numpy Arrays
#############################################

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=10)

a.ndim
a.shape
a.size
a.dtype

#############################################
# Reshaping
#############################################

np.arange(1, 10)
np.arange(1, 10).reshape((3, 3))

#############################################
# Index Selection
#############################################

a = np.random.randint(10, size=10)
a[0]
a[-2]
a[0] = 999
a
a[0:4]

m = np.random.randint(10, size=(3, 5))
m
m[0, 0]
m[1, 1]
m[2, 3]
m[2, 3] = 9999

m
m[2, 3] = 2.9
m
m
m[:, 0]
m[1, :]
m[0:2, 0:3]

#############################################
# Fancy Index
#############################################

v = np.arange(0, 30, 3)
v

v[1]
v[4]
v[3]

catch = [1, 6, 3]
v[catch]

#############################################
# Conditions on Numpy
#############################################

v = np.array([1, 2, 3, 4, 5])
type(v)

# klasik dongu

ab = []

for i in v:
    if i < 3:
        ab.append(i)

v

v[v < 3]
v[v > 3]
v[v >= 3]

# Matematiksel işlemler

v = np.array([1, 2, 3, 4, 5])
v / 5
v * 5 / 10
v ** 2
v - 1
v * 5

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
v.sum()
v.min()

#############################################
# PANDAS
#############################################

# Panel Data
# Veri manipülasyonu ve veri analizi için yazılmış açık kaynak kodlu bir Python kütüphanesidir.
# Ekonometrik ve finansal çalışmalar için doğmuştur.
# Temeli 2008 yılında atılmıştır.
# Bir çok farklı veri tipini okuma ve yazma imkanı sağlar.

# Reading Data
# Selection in Pandas
# iloc & loc
# Conditional Selection
# Aggregation & Grouping
# Apply
# Pivot table
# Num to Cat
# Combining Two Dataframes and Dublicated Rows

#############################################
# Reading Data
#############################################

import pandas as pd

df = pd.read_csv('datasets/titanic.csv')
type(df)

df.head()
df.tail()
df.shape
df.info()
df.columns
df.columns.values
df.columns.values[0]
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df.isna().sum()
df.notna().sum()
df["Sex"].value_counts()
df["Embarked"].value_counts()

#############################################
# Selection in Pandas
#############################################

### Index Üzerinde İşlemler ###

df.index

df[13:18]
df.head()
df.drop(0, axis=0).head()
df.head()
# df.drop(0, axis=0, inplace=True)

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

#############################################
# Col to Index
#############################################


df.head()

df.sort_values("PassengerId", ascending=False).head()

df.index = df["PassengerId"]

# 1. yol
df.drop("PassengerId", axis=1).head()

# 2. yol
df.loc[:, df.columns != 'PassengerId'].head()

df.drop("PassengerId", axis=1, inplace=True)

#############################################
# Index to Col
#############################################

df["PassengerId"] = df.index
df.head()

df.drop("PassengerId", axis=1, inplace=True)

df.reset_index().head()
df.reset_index(drop=True).head()

df.reset_index(inplace=True)
df.head()

### Değişkenler Üzerinde İşlemler ###

"Age" in df
df.head()
df["Age"].head()
df.Age.head()

df[["Age", "PassengerId"]].head()

col_names = ["Age", "Embarked", "Ticket"]

df[col_names].head()

col_names = [col for col in df.columns if df[col].dtypes != "O"]
df[col_names]
df["Age2"] = df["Age"] ** 2

df.head()

df["Age3"] = df["Age"] / df["Age2"]

df.drop("Age3", axis=1).head()

col_names = ["Age", "Embarked", "Ticket"]
df.drop(col_names, axis=1).head()

col_names = [col for col in df.columns if "Age" in col]
col_names = [col for col in df.columns if "Age" not in col]

df[col_names].head()

df.loc[:, df.columns.str.contains('Age')].head()
df.loc[:, ~df.columns.str.contains('Age')].head()

df.head()

df.values

for row in df.values:
    print(row)

#############################################
# iloc & loc
#############################################

# iloc: integer based selection
df.head()
df.iloc[0:3]
df.iloc[0, 0]

# loc: label based selection
df.loc[0:3]

df[0:3]

df[0:3, 0:2]
df[0:3, "Age"]
df.iloc[0:3, 0:2]
df.iloc[0:3, "Age"]
df.loc[0:3, "Age"]

col_names = ["Age", "Embarked", "Ticket"]
df.loc[0:3, col_names]

#############################################
# Conditional Selection
#############################################

df[df["Age"] > 50].head()

df["Age"][df["Age"] > 60].count()

df[df["Age"] > 60]["Name"]

df[df["Age"] > 60]["Age"].nunique()

df.loc[df["Age"] > 60, "Name"].head()

df[(df["Age"] > 50) & (df["Sex"] == "female")].head()

#############################################
# Aggregation & Grouping
#############################################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()

# cinsiyete göre yolcu sayısı
df[["PassengerId", "Sex"]].groupby("Sex").agg({"count"})

# 50'den buyuk cinsiyete göre yolcu sayısı nedir?
df[df["Age"] > 50][["PassengerId", "Sex"]].groupby("Sex").agg({"count"})

df.loc[df["Age"] > 50, ["PassengerId", "Sex"]].groupby("Sex").agg({"count"})

df.loc[df["Age"] > 50, ["PassengerId", "Sex"]].groupby("Sex").agg(["count", "mean"])

df[["PassengerId", "Age", "Sex"]].groupby("Sex").agg({"PassengerId": "count",
                                                      "Age": "mean"})

df.loc[df["Age"] > 50, ["PassengerId", "Age", "Sex"]].groupby("Sex").agg({"PassengerId": "count",
                                                                          "Age": "mean"})

df[["PassengerId", "Age", "Sex"]].groupby("Sex").agg({"PassengerId": "count",
                                                      "Age": ["mean", "min", "max"]})

df.groupby(["Sex", "Embarked"]).agg({"PassengerId": "count",
                                     "Age": ["mean", "min", "max"]})

df.groupby(["Sex", "Embarked", "Pclass"]).agg({"PassengerId": "count",
                                               "Age": ["mean"],
                                               "Survived": ["mean"]})

agg_functions = ["nunique", "first", "last", "sum", "var", "std"]


df.groupby(["Sex", "Embarked", "Pclass"]).agg({"PassengerId": "count",
                                               "Age": agg_functions})


#############################################
# Apply
#############################################
df.head()

(df["Age"]**2).head()
(df["Age2"] ** 2).head()
(df["Age3"] ** 2).head()


for col in df.columns:
    if "Age" in col:
        print(col)



for col in df.columns:
    if "Age" in col:
        print((df[col]**2).head())


for col in df.columns:
    if "Age" in col:
        df[col] = df[col]**2

df.head()

df[["Age", "Age2", "Age3"]].apply(lambda x: x ** 2).head()

df.loc[:, df.columns.str.contains('Age')].apply(lambda x: x ** 2).head()

df.loc[:, df.columns.str.contains('Age')].apply(lambda x: (x - x.mean()) / x.std()).head()

df[["Age"]].apply(lambda x: (x - x.mean()) / x.std()).head()

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

standart_scaler(df[["Age"]]).head()




df[["Age"]].apply(standart_scaler).head()

df.loc[:, df.columns.str.contains('Age')].apply(standart_scaler).head()
df.head()

df.loc[:, ["Age", "Age2", "Age3"]] = df.loc[:, df.columns.str.contains('Age')].apply(standart_scaler)
df.head()

#############################################
# Pivot table
#############################################

df = pd.read_csv('datasets/titanic.csv')
df.head()

df.pivot_table(values="Age", index="Sex", columns="Embarked")

df.pivot_table(values="Age", index="Sex", columns="Embarked", aggfunc="std")


#############################################
# Num to Cat
#############################################

df.head()
df["new_age"] = pd.cut(df["Age"], [0, 10, 18, 25, 40, 90])
df[["Age", "new_age"]].head()

df.pivot_table("Survived", index="Sex", columns="new_age")

df.pivot_table("Survived", index=["Sex", "Pclass"], columns="new_age")

#############################################
# Combining Two Dataframes and Dublicated Rows
#############################################

users = pd.read_csv('datasets/users.csv')
users.head()

users.shape

users["uid"].nunique()

purchases = pd.read_csv('datasets/purchases.csv')
purchases.head()
purchases.shape
purchases["uid"].nunique()

purchases["uid"].value_counts()


#####################
# AMAC 1: Satın almalarla ilgili daha fazla bilgi istiyoruz. (left join)
#####################

df = purchases.merge(users, how="left", on="uid")
df.shape
df["uid"].nunique()

purchases.head()
df.head()


#####################
# AMAC 2: Tüm User'lara odaklanmak ve analiz yapmak
#####################


df = users.merge(purchases, how='left', on='uid')
df.head()

df.shape

df["uid"].nunique()

df[df["uid"] == 41195147]

a = df.groupby(["uid", "device"]).agg({"device": "nunique"})
a[a["device"] > 1]


df.groupby("uid").agg({"date": "max"}).head()

df.groupby("uid").agg({"price": ["mean"]}).head()

df.groupby("uid").agg({"uid": ["count"]}).head()

agg_df = df.groupby("uid").agg({"date": "max",
                                "price": ["mean"],
                                "uid": ["count"]})

agg_df.head()
agg_df.reset_index(inplace=True)

agg_df.columns

[col[0] + "_" + col[1] if col[1] else col[0] for col in agg_df.columns]

agg_df.columns = [col[0] + "_" + col[1] if col[1] else col[0] for col in agg_df.columns]

df.head()

all_data = users.merge(agg_df, how="left", on="uid")
all_data.head()
all_data.shape

all_data["uid"].nunique()

all_data["uid_count"] = all_data["uid_count"] - 1
all_data.head()


#############################################
# ÖDEVLER
#############################################

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
# PROJE: LEVEL BASED PERSONA TANIMLAMA, BASIT SEGMENTASYON ve KURAL TABANLI SINIFLANDIRMA
#############################################

# Proje Amacı:
# - Persona kavramını düşünmek
# - Level'lara göre yeni müşteri tanımları yapabilmek
# - qcut fonksiyonunu kullanarak basitçe yeni müşteri tanımlarını segmentlere ayırmak. price'a göre.
# - Yeni bir müşteri geldiğinde bu müşteriyi segmentlere göre sınıflandırmak.

# Hedefimiz tekil olarak var olan müşteriler için önce gruplandırmalar yapmak (level based persona tanımlama)
# sonra da bu grupları segmentlere ayırmaktır.
# Son olarak da yeni gelebilecek bir müşterinin bu segmentlerden hangisine ait olduğunu belirlemeye çalışmaktır.
# Elde edilmesi gereken çıktı öncesi ve sonrası ile aşağıdaki şekilde olacaktır:

################# Önce #####################
#
# country device gender age  price
# USA     and    M      15   61550
# BRA     and    M      19   45392
# DEU     iOS    F      16   41602
# USA     and    F      17   40004
#                M      23   39802

################# Sonra #####################
#
#   customers_level_based      price groups
# 0        USA_AND_M_0_18 157120.000      A
# 1        USA_AND_F_0_18 151121.000      A
# 2        BRA_AND_M_0_18 149544.000      A
# 3        USA_IOS_F_0_18 133773.000      A
# 4       USA_AND_F_19_23 133645.000      A


# AŞAĞIDAKİ SORULARA GÖRE ADIM ADIM SONUCA ULAŞABİLİRSİNİZ.

# 1. users ve purchases veri setlerini okutunuz ve veri setlerini "uid" değişkenine göre inner join ile merge ediniz.

# İpucu:
# users = pd.read_csv()
# purchases = pd.read_csv()
# df = purchases.merge()


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

# 4. agg_df'in index'lerini değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan price dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()

# 5. age değişkenini kategorik değişkene çeviriniz ve agg_df'e "age_cat" ismiyle ekleyiniz.
# Aralıkları istediğiniz şekilde çevirebilirsiniz fakat ikna edici olmalı.

# Elde edilmesi gereken çıktı:

#   country device gender  age  price age_cat
# 0     USA    and      M   15  61550    0_18
# 1     BRA    and      M   19  45392    0_18
# 2     DEU    iOS      F   16  41602    0_18
# 3     USA    and      F   17  40004    0_18
# 4     USA    and      M   23  39802   19_23



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


# Segmentleri betimleyiniz çıktısı:

#             price
# segment
# D        1335.096
# C        3675.505
# B        7447.812
# A       20080.150


# 8. 42 yaşında IOS kullanan bir Türk kadını hangi segmenttedir?
# agg_df tablosuna göre bu kişinin segmentini (grubunu) ifade ediniz.
# İpucu: new_user = "TUR_IOS_F_41_75"

# Çıktı:
#     customers_level_based  price segment
# 377       TUR_IOS_F_41_75   1596       D



################
# AFTER PARTY
################

# Problem neydi? purchases'ta yer alan tüm id'lerin users'ta da olup olmadığını doğrulamak.

df = purchases.merge(users, how='left', on='uid')
df.shape
df["uid"].nunique()
ser_u = pd.Series(np.union1d(purchases["uid"], users["uid"]))
ser_i = pd.Series(np.intersect1d(purchases["uid"], users["uid"]))
ser_u[~ser_u.isin(ser_i)].count()
purchases["uid"].nunique() + ser_u[~ser_u.isin(ser_i)].count()
purchases[purchases["uid"].isin(ser_u[~ser_u.isin(ser_i)])]


######################################
# AFTER PARTY: reset_index problems
######################################

df.groupby(["uid", "device"]).agg({"device": "nunique"}).head()

df.groupby(["uid", "device"]).agg({"device": "nunique"})[["device"]].sort_values("device").head()

a = df.groupby(["uid", "device"]).agg({"device": "nunique"})

a.reset_index(level=1, drop=True).head()
a.reset_index(level=1, drop=True, inplace=True)

a.reset_index().head()
a.reset_index(inplace=True)
a.head()


a.sort_values(by="device", ascending=False).head()

a[a["device"]>1]

a.groupby()
df.groupby(["uid", "device"], as_index=False).agg({"device": "nunique"}).sort_values("device", ascending=False)


#############################################
# FUNCTIONAL EXPLORATORY DATA ANALYSIS
#############################################

# 1. GENEL RESIM
# 2. KATEGORIK DEGISKEN ANALIZI
# 3. SAYISAL DEGISKEN ANALIZI
# 4. TARGET ANALIZI
# 5. SAYISAL DEGISKENLERIN BIRBIRLERINE GORE ANALIZI


#############################################
# 1. GENEL RESIM
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
df = pd.read_csv("datasets/titanic.csv")

df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

#############################################
# 2. CATEGORICAL VARIABLES
#############################################

df["Sex"].value_counts()
df["Sex"].unique()
df["Sex"].nunique()

cat_cols = [col for col in df.columns if df[col].dtypes == "O"]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes != "O"]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtypes == "O"]


cat_cols
num_but_cat
cat_but_car

final_cat_cols = cat_cols + num_but_cat

final_cat_cols = [col for col in final_cat_cols if col not in cat_but_car]

df[final_cat_cols].nunique()

for col in final_cat_cols:
    print(df[col].value_counts())
    print(100 * df[col].value_counts() / len(df))
    sns.countplot(x=df[col], data=df)
    plt.show()

final_cat_cols


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("######################################################")
    sns.countplot(x=dataframe[col_name], data=dataframe)
    plt.show()

cat_summary(df, "Survived")


for col in final_cat_cols:
    cat_summary(df, col)



def cat_summary_adv(dataframe, categorical_cols, number_of_classes=10):
    col_count = 0
    cols_more_classes = []
    for col in categorical_cols:
        if dataframe[col].nunique() <= number_of_classes:
            print(pd.DataFrame({col: dataframe[col].value_counts(),
                                "Ratio (%)": round(100 * dataframe[col].value_counts() / len(dataframe), 2)}),
                  end="\n\n\n")
            col_count += 1
        else:
            cols_more_classes.append(dataframe[col].name)

    print(f"{col_count} categorical variables have been described.\n")
    if len(cols_more_classes) > 0:
        print(f"There are {len(cols_more_classes)} variables which have more than {number_of_classes} classes:")
        print(cols_more_classes)

cat_summary_adv(df, final_cat_cols)
cat_summary_adv(df, cat_cols, 500)


#############################################
# 3. NUMERIC VARIABLES
#############################################

df.describe().T
num_cols = [col for col in df.columns if df[col].dtypes != 'O']

df[["Age", "Fare"]].describe([0.05, 0.10, 0.25, 0.50, 0.75, 0.80, 0.90, 0.95, 0.99]).T

df.drop("PassengerId", axis=1).columns


num_cols = [col for col in df.columns if df[col].dtypes != 'O']

num_cols = [col for col in df.columns if df[col].dtypes != 'O' and col not in ["PassengerId", "Survived"]]

num_cols = [col for col in num_cols if col not in final_cat_cols]
final_cat_cols
cat_but_car
id_col = 'PassengerId'

num_cols

df["Age"].hist(bins=30)
plt.show()

sns.boxplot(x=df["Age"])
plt.show()


def num_hist(dataframe, numeric_col):
    col_counter = 0
    for col in numeric_col:
        dataframe[col].hist(bins=20)
        plt.xlabel(col)
        plt.title(col)
        plt.show()
        col_counter += 1
    print(f"{col_counter} variables have been plotted")


num_hist(df, num_cols)


df = pd.read_csv("datasets/application_train.csv")
df.shape
df.head()

num_cols = [col for col in df.columns if df[col].dtypes != 'O' and
            col not in ["SK_ID_CURR ", "TARGET"]]

df.shape[1] - len(num_cols)

num_hist(df, num_cols)

num_cols = [col for col in df.columns if df[col].dtypes != 'O' and
            df[col].nunique() > 20 and
            col not in ["SK_ID_CURR ", "TARGET"]]

num_hist(df, num_cols)


df = pd.read_csv("datasets/application_train.csv")


def grab_cat_names(dataframe, cat_th=10, car_th=20):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    final_cat_cols = cat_cols + num_but_cat
    final_cat_cols = [col for col in final_cat_cols if col not in cat_but_car]
    return cat_cols, num_but_cat, cat_but_car, final_cat_cols


cat_cols, num_but_cat, cat_but_car, final_cat_cols = grab_cat_names(df)


len(final_cat_cols)

df[final_cat_cols].head()

for col in final_cat_cols:
    cat_summary(df, col)


#############################################
# 4.TARGET
#############################################
def load_titanic():
    df = pd.read_csv("datasets/titanic.csv")
    return df

df = load_titanic()


df = pd.read_csv("datasets/titanic.csv")
df["Survived"].value_counts()
df["Survived"].mean()
cat_summary(df, "Survived")


#############################################
# KATEGORIK DEGISKENLERE GORE TARGET ANALIZI
#############################################


df.groupby("Sex")["Survived"].mean()

cat_cols, num_but_cat, cat_but_car, final_cat_cols = grab_cat_names(df)

final_cat_cols

def target_summary_with_cat(dataframe, categorical_cols, target):
    for col in categorical_cols:
        if col not in target:
            print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(col)[target].mean()}), end="\n\n\n")

target_summary_with_cat(df, final_cat_cols, "Survived")

def load_app_train():
    df = pd.read_csv("datasets/application_train.csv")
    return df


df = load_app_train()

cat_cols, num_but_cat, cat_but_car, final_cat_cols = grab_cat_names(df)

target_summary_with_cat(df, final_cat_cols, "TARGET")


#############################################
# SAYISAL DEGISKENLERE GORE TARGET ANALIZI
#############################################

df = load_titanic()
df.groupby("Survived").agg({"Age": "mean"})
df.groupby("Survived").agg({"Fare": "mean"})


num_cols = [col for col in df.columns if df[col].nunique() > 10
            and df[col].dtypes != 'O'
            and col not in ["Survived", "PassengerId"]]

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")

target_summary_with_num(df, "Survived", "Age")

for col in num_cols:
    target_summary_with_num(df, "Survived", col)


df = load_app_train()

num_cols = [col for col in df.columns if df[col].nunique() > 10
            and df[col].dtypes != 'O'
            and col not in ["TARGET", "SK_ID_CURR"]]

for col in num_cols:
    target_summary_with_num(df, "TARGET", col)



#############################################
# 5.SAYISAL DEGISKENLERIN BIRBIRLERINE GORE INCELENMESI
#############################################

df = sns.load_dataset("tips")
df.head()
df.info()

sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()

sns.lmplot(x="total_bill", y="tip", data=df)
plt.show()

df.corr()


# chi-squared: iki kategorik değişkenin bağımsızlığını test eder.


#########################
# ODEVLER
#########################

#########################
# ZORUNLU ÖDEV: grab_col_names adında değişken tiplerini return eden bir fonksiyon yazınız.
# Kategorik ve sayısal değişken isimlerini return eden bir fonksiyon yazılmalıdır.
# Herhangi bir kısıt olmadan direk tipi 0 olanları kategorik, 0 olmayanları numerik olarak seçiniz.
#########################

# Beklenen çıktı:
# df = pd.read_csv("datasets/titanic.csv")
# cat_cols, num_cols = grab_col_names(df)
# print(cat_cols)
# ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
# print(num_cols)
# ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

#############################################
# ZORUNLU ÖDEV: Aşağıdaki özellikleri taşıyan summary adında bir fonksiyon yazınız.
#############################################

# Bir dataframe verildiğinde bu dataframe'i aşağıdaki başlıklarda özetlesin:
# 1. Veri setindeki gözlem sayısı
# 2. Veri setindeki değişken sayısı
# 3. Kategorik değişken sayısı
# 4. Sayısal değişken sayısı
# 5. Sayısal değişken ama 20 sınıf ya da daha az sayıda sınıfı olan değişken sayısı (num_but_cat)
# 6. Kategorik fakat sınıf sayısı çok fazla olan değişken sayısı (20) (cat_but_car)
# Hatırlatma: Aynı satırda print: print(f" Observations: {df.shape[0]}")

# Beklenen çıktı:
# df = pd.read_csv("datasets/titanic.csv")
# summary(df)
# Observations: 891
# Variables: 12
# Categorical Variables: 5 (Cat but Car Variables: 3)
# Numerical Variables: 7 (Num but Cat Variables: 4)


#########################
# KEYFI ODEV:
#########################
# cat_cols, num_but_cat, cat_but_car, final_cat_cols bu listeler return edilsin.
# num_cols return edilsin
# varsa target return edilesin.
# varsa id değişken return edilsin.
# ÇOK ÖNEMLİ NOKTA!
# fonksiyon return etmeden önce ilk df.shape[1] ile tüm return edecek list eleman toplamı
# aynı olmalıdır.

def grab_col_lists(dataframe, cat_th=10, car_th=20):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    final_cat_cols = cat_cols + num_but_cat
    final_cat_cols = [col for col in final_cat_cols if col not in cat_but_car]
    return cat_cols, num_but_cat, cat_but_car, final_cat_cols


cat_cols, num_but_cat, cat_but_car, final_cat_cols = grab_cat_names(df)