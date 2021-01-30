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

import pandas as pd

df = pd.read_csv("./datasets/titanic.csv")
df.head()
df.info()

def grab_col_names(dataframe):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    #num_cols = [col for col in dataframe.columns if dataframe[col].dtypes !='O']
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ['float64', 'int64'] ]
    return cat_cols, num_cols

cat_cols, num_cols = grab_col_names(df)

print(cat_cols)
print(num_cols)


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


import pandas as pd

df = pd.read_csv("./datasets/titanic.csv")
df.head()
df.info()

def summary(dataframe, **kwargs):
    # print out number of observation and variables
    dataframe_shape = dataframe.shape
    print(f'Observations: {dataframe_shape[0]}')
    print(f'Variables: {dataframe_shape[1]}')

    # define column list categorizer function in to four different segments for dataframes
    def grab_col_lists(dataframe, cat_th=10, car_th=20):
        cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
        num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
        num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                       dataframe[col].dtypes != "O"]
        cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                       dataframe[col].dtypes == "O"]
        return cat_cols, num_cols, num_but_cat, cat_but_car

    cat_cols, num_cols, num_but_cat, cat_but_car = grab_col_lists(dataframe, **kwargs)

    # print out number of four different column lists
    print(f'Categorical Variables: {len(cat_cols)} (Cat but Car Variables: {len(cat_but_car)})')
    print(f'Numerical Variables: {len(num_cols)} (Num but Cat Variables: {len(num_but_cat)})')

# categoric and cardinal threshold values can be specified as cat_th=20, car_th=20
summary(df, cat_th=20, car_th=20)
summary(df)