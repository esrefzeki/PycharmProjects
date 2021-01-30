import pandas as pd
df = pd.read_csv('train.csv')
pd.set_option('display.max_columns', None)

#grap_colsadında bir fonksiyon tanımlayınız
#ve bu fonksiyon kendisine sorulan dataframe’in tüm olası farklı değişken türlerine göre değişken isimlerini return etsin.
#cat_colsnum_but_catcat_but_carfinal_cat_cols num_cols target id date
#Dikkat!
#Not: Fonksiyon return etmeden önce ilk df.shape[1] ile tüm return edilecek listelerdeki eleman toplamlarıaynı olmalıdır.


target = input("Target: ")
def grab_col_lists(dataframe, number_of_classes = 20):
    cat_cols = [i for i in dataframe.columns if dataframe[i].dtypes == "object"]
    num_cols = [i for i in dataframe.columns if dataframe[i].dtypes != "object"]
    num_but_cat = [i for i in dataframe.columns if dataframe[i].nunique() < number_of_classes and
                       dataframe[i].dtypes != "object"]
    cat_but_car = [i for i in dataframe.columns if dataframe[i].nunique() > number_of_classes and
                       dataframe[i].dtypes == "object"]
    final_cat_cols = cat_cols + num_but_cat
    final_cat_cols = [i for i in final_cat_cols if i not in cat_but_car]
    final_num_cols = [i for i in dataframe.columns if dataframe[i].dtypes != "object" and i not in num_but_cat]
    target = [i for i in dataframe.columns if "target" in str(dataframe[i]).lower()]
    id = [i for i in dataframe.columns if "_id" in str(dataframe[i]).lower()]
    date = [i for i in dataframe.columns if "days" in str(dataframe[i]).lower()]
    return cat_cols, num_cols, num_but_cat, cat_but_car, final_cat_cols, final_num_cols, target, id, date



def summary(dataframe, number_of_classes=20):
        cat_cols, num_cols, num_but_cat, cat_but_car, final_cat_cols, final_num_cols, target, id,date = grab_col_lists(dataframe)
        print(f'Variables: {dataframe.shape[1]}')
        print(f'Categorical Variables: {len(cat_cols)}, {cat_cols}')
        print(f'Numerical Variables: {len(num_cols)}, {num_cols}')
        print(f'Num but Cat Variables: {len(num_but_cat)}, {num_but_cat}')
        print(f'Cat but Car Variables: {len(cat_but_car)}, {cat_but_car}')
        print(f'Final Cat Cols: {len(final_cat_cols)}, {final_cat_cols}')
        print(f'Final Num Cols: {len(final_num_cols)}, {final_num_cols}')
        print("target:", target)
        print("id:", id)
        print("date", date)
        print("****************DONE*****************")

summary(df)