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
# df = sns.load_dataset("titanic")
df = pd.read_csv("/Users/esrefzekiparlak/PycharmProjects/pythonProject1/titanic.csv")

df.head() # Verilerin ilk 5 verisini gösterir
df.tail() # Verilerin son 5 verisini gösterir
df.shape # Verilerin ne kadar değişken ve kategoriden oluştuğunu gösterir
df.info() # Veriye ait tüm detayları rapor şeklinde gösterir
df.columns # Verideki sütunları gösterir
df.index # Verideki index bilgilerini gösterir
df.describe().T # Verinin transpozunu alarak analiz etmemiz için numerik verileri değerlendirir
df.isnull().values.any() # Hergangi NaN değer var ise True olarak gösterir
df.isnull().sum() # Kategorik içeriğe göre sahip olduğu toplam NaN içerik sayısını gösterir

#############################################
# 2. CATEGORICAL VARIABLES
#############################################

df["Sex"].value_counts() # Kategorik içerisinde yer alan alt kategori değişken sayını saydırır
df["Sex"].unique() # Kategori içerisindeki başlıkları ve veri tiplerini(dtype) gösterir
df["Sex"].nunique() # Kategori içerisindeki başlıkların kaç adet olduğunu gösterir

# Burada 'object' olarak yer alan kategorik başlıkları aratıp bulduruyoruz
cat_cols = [col for col in df.columns if df[col].dtypes == "O"]

# Burada df.columns içerisinde yer alan bağımsız değişken sayısının 10'dan az olan ve object
# olmayan sütunlarını bulduruyoruz ve num_but_cat olarak atama yapıyoruz
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes != "O"]

# Burada ise yukarının tersi olarak 20'den fazla bağımsız değişkenin olduğu ve object olan
# kategorik değişkenleri seçip cat_but_car olarak atamasını yapıyoruz
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtypes == "O"]

# Yukarıdaki atanan kategori başlıklarını çağırıyoruz:
cat_cols
num_but_cat
cat_but_car

# İki farklı kategoriyi birleştirerek çağırıyoruz:
final_cat_cols = cat_cols + num_but_cat
# Böylelikle iki sütun bilgisini istediğimiz formata sokarak birleştirme
# işlemi gerçekleştiriyoruz

# Burada yukarıda birleşen iki kategorik başlık içeriğinin üçüncü bir kategorik değişken
# başlığının içeriğini çıkartıyoruz ve final_cat_cols 'a atıyoruz
final_cat_cols = [col for col in final_cat_cols if col not in cat_but_car]

# Yukarıdaki işlemdeki değişikliğin sonucunu görmek için aşağıdaki gibi değişen değerleri
# aşağıdaki kodu çağırarak teyit ediyoruz
df[final_cat_cols].nunique()

# final_cat_cols içeriğinde yer alan başlıkların içerisinde gezinip, value_count ile kategorik
for col in final_cat_cols:
    print(df[col].value_counts())
    # değişkenin içinde yer alan değerleri saydırıyoruz.
    print(100 * df[col].value_counts() / len(df))
    # col içerisinde yer alan value_counts değerlerini 100 ile çarpıp df içerik toplam değerine bölüyoruz
    sns.countplot(x=df[col], data=df)
    # seaborn kütüphanesinin içerisinden verileri görselleştirmek için
    # x yatay koordinat sistemine df sütunlarını yerleştirip verileri
    #data ataması ile df'ten alması gerektiğini belirtiyoruz
    plt.show()
    # Ve sonucu görsel üzerinde görmek için bu fonksiyonu çağırıyoruz.

final_cat_cols

# dataframe ve col_name değerlerini içerek bir cat_summary fonksiyonu oluşturuyoruz
def cat_summary(dataframe, col_name):
    # Aşağıda pandas ile dataframe oluşturuyoruz ve içerisinde bir dictionary oluşturuyoruz
    # ve bu liste içerisine col_name ataması olarak dataframe içerisinde yer alan col_name
    # value_counts'unu atıyoruz
    # "Ratio" değişkenini de aşağıdaki hesaba göre değerler barındırmasını söylüyoruz ve dataframe uzunluğuna bölmesini sağlıyoruz
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("######################################################")
    # sns.countplot grafiği ile aşağıda x düzleminde yer alması gerektiği ve verileri
    # data = ile dataları alacağı yeri belirtip plt.show() ile göstermesini sağlıyoruz
    sns.countplot(x=dataframe[col_name], data=dataframe)
    plt.show()

cat_summary(df, "Survived") # En son değişkenleri fonksiyona göre yerleştirip fonksiyonu çalıştırıyoruz


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