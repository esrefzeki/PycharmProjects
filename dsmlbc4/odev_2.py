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

df = pd.read_csv("titanic.csv")
df.head()
df.info()

def grab_col_names(dataframe):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ['float64', 'int64']]
    #Diğer alternatif: num_cols = [col for col in dataframe.columns if dataframe[col].dtypes !='O']
    return cat_cols, num_cols

cat_cols, num_cols = grab_col_names(df)

print(cat_cols)
print(num_cols)
