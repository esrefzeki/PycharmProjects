import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


#Maximum Bidding(Control)
control_group = pd.read_excel(r'C:\Users\yilma\PycharmProjects\DSMLBC-4\datasets\ab_testing_data.xlsx', 'Control Group')
#Average Bidding(Test)
test_group = pd.read_excel(r'C:\Users\yilma\PycharmProjects\DSMLBC-4\datasets\ab_testing_data.xlsx', 'Test Group')

#Maximum Bidding(Control)
control_group.head()
control_group.isnull().sum()
control_group.describe([0, 0.05, 0.50, 0.95, 0.99]).T

#Average Bidding(Test)
test_group.head()
test_group.isnull().sum()
test_group.describe([0, 0.05, 0.50, 0.95, 0.99]).T

#control groups mean
control_group["Purchase"].mean()

#test groups mean
test_group["Purchase"].mean()


#Feature Engineering

#conversion rate

control_group['Conversion_Rate'] = control_group['Purchase'] / control_group['Click'] * 100
test_group['Conversion_Rate'] = test_group['Purchase'] / test_group['Click'] * 100

#satın alma başına kazanç
control_group['Earning_per_Purchase'] = control_group['Earning'] / control_group['Purchase'] * 100
test_group['Earning_per_Purchase'] = test_group['Earning'] / test_group['Purchase'] * 100

#tıklama oranı
control_group['Click_Through_Rate'] = control_group['Click'] / control_group['Impression'] * 100
test_group['Click_Through_Rate'] = test_group['Click'] / test_group['Impression'] * 100

control_group['Group'] = "C"
test_group['Group'] = "T"

AB_test = pd.concat([control_group, test_group], ignore_index=True)
cols = AB_test.columns
AB_test.shape
for col in cols :
    sns.boxplot(x ="Group", y = col, hue = "Group", data = AB_test)
    plt.show()

#NORMALLIK VARSAYIMI
# H0: iki orneklem icin normallik varsayimi saglanmaktadir.
# H1: iki orneklem icin normallik varsayimi saglanmamaktadir.
shapiro(control_group['Purchase'])
#p value > 0.05 H0 hipotezi control grubu icin reddedilemedi, normallik varsayimi saglaniyor

shapiro(test_group['Purchase'])
#p value > 0.05 H0 hipotezi test grubu icin reddedilemedi, normallik varsayimi saglaniyor

#VARYANS HOMOJENLIGI
#H0: varyanslar homojendir
#H1: varyanslar homojen degildir
levene(control_group['Purchase'], test_group['Purchase'])
#p value > 0.05 H0 hipotezi reddedilemedi, varyanslar homojendir

#BAGIMSIZ IKI ORNEKLEM T TESTI
#HO: iki grup arasinda istatistiki olarak anlamli bir farklilik yoktur
#H1: iki grup arasinda istatistiki olarak anlamli bir farklilik vardir
ttest_ind(control_group['Purchase'],test_group['Purchase'], equal_var=True)
#p value > 0.05 H0 hipotezi reddedilemedi, iki grup arasinda anlamli bir farklilik yoktur

"""Sorular
1.AB testinin hipotezini nasıl tanımlarsınız?
2.İstatistiki olarak anlamlı sonuç çıkarabilir miyiz?
3.Hangi testi kullandınız, neden?
- İki örneklem de normallik ve varyans homojenliği varsayımlarını sağladığı için Bağımsız İki Örneklem T Testi kullanıldı
4.Soru 2'ye verdiğiniz cevaba göre müşteriye tavsiyeniz nedir?"""
