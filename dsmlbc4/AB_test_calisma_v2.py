#Facebook maximum bidding, average bidding yöntemlerinden hangisinin
# daha iyi olduğunu istatistiki olarak belirleyip müşterinizi ikna ediniz.


import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
df_control = pd.read_excel("ab_testing_data.xlsx",sheet_name = "Control Group") # maximum bidding
df_test = pd.read_excel("ab_testing_data.xlsx",sheet_name = "Test Group") #average bidding (

# kontrol grubu :var olan teknoloji -> maximum bidding
# test grubu : yeni teknoloji -> average bidding

#1 Iki grubun purchase degerlerinin karsilastirilmasi


# Iki grubun satislarini görsel olarak karsilastirma

#eda ->Function will be written here


#Checking the missing values
df_control.isnull().values.any() #False
df_test.isnull().values.any() #False

#There isn't any missing values in data set.

pd.set_option('display.max_columns', None)

#Comparison of two bidding types
df_control["Purchase"].mean()
df_control["Purchase"].describe().T
df_test["Purchase"].describe().T
df_test["Purchase"].mean()

df_control.head()
df_test.head()

# Soru: Carpikligi ve basikligi tek bir yerden test yapmadan görebilecegimiz
# bir yer var miydi?

## Combining two data sets for visualization

# if Purchase in "df_control" ->Purchase_maximum_bidding
# if Purchase in "df_test" ->Purchase average bidding

control_cols = [col+"_av_bid" for col in df_control.columns]
df_control.columns = control_cols
df_control.head()

test_cols = [col+"_max_bid" for col in df_test.columns]
df_test.columns = test_cols
df_test.head()

df_all = pd.concat([df_control, df_test], axis =1)
df_all.head()

df_purchase = df_all[["Purchase_av_bid","Purchase_max_bid"]]
df_purchase.head()


sns.boxplot(x="variable",y="value",data= pd.melt(df_purchase))
plt.show()

# https://incipia.co/post/app-marketing/facebook-ads-launches-average-cost-and-maximum-cost-bidding/

# Avarage Bidding(Ihale): Facebook, ortalama maliyet teklifinin "herhangi bir sonuç için ödemeye
# hazır olduğunuz maksimum tutar yerine ortalama sonuç başına maliyetinizin ne olmasını
# istediğinizi bize söylemenizi sağladığını açıklıyor. Bu tür bir teklif vermeyi
# kullanırsanız, İstediğiniz ortalama maliyeti göz önünde bulundurarak size olabildiğince
# çok sonuç almaya çalışın. "


# Maximum Bidding(Ihale): Facebook, maksimum maliyet teklifinin "bize bir sonuç için
# ödemek istediğiniz maksimum tutarı söylemenizi sağladığını açıklıyor. Bu tür bir
# teklif vermeyi kullanırsanız, size eşit
# bir fiyata mümkün olduğunca çok sonuç almaya çalışacağız. veya teklifinizden daha az. "

# AB Test icin Varsayim kontrolü
#1. Normal dagilim kontrolü
# (Iki grup icin ayri ayri bakilir.Iki grupta biri bile saglazmasa varsayim saglanmaz.)
#2. Varyans homojenligi kontrolü ( Iki grup icin birlikte bakilir)
#https://drive.google.com/file/d/1jhg8odkcagOXJg_myWZrgZsdmM-gkXgL/view?usp=sharing

## Varsayimlar icin H0 varsayim saglandi seklinde yazilir.Varsayimlarda
# reddetmek istemeyiz.
#H0 her zaman esitlik uzerine yani fark olmamasi uzerine kurulur.

## Normallik varsayımı kontrolü

# Her iki grup icin tek tek bakilir.

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dagilim varsayimi sağlanmamaktadır.

from scipy.stats import shapiro

test_istatistigi, pvalue = shapiro(df_control["Purchase"])
print('Kontrol Grubu Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue)) #p-değeri = 0.5891
# p >0.05 ->H0 reddedilmedi. Yani kontrol grubu icin normallik varsayimi saglanmaktadir.

test_istatistigi, pvalue = shapiro(df_test["Purchase"])
print('Test Grubu Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue)) # p-değeri = 0.1541
# p >0.05 ->H0 reddedilmedi. Yani kontrol grubu icin normallik varsayimi saglanmaktadir.

# H0 hipotezi reddedilemez ikisi icin de. Ikisi de normal dagilmis.

# Varyans Homojenliği Varsayımı
# (H0: Varyanslar homojendir)
# (H1: Varyanslar homojen degildir)

from scipy.stats import levene
test_istatistigi, pvalue = levene(df_control["Purchase"],df_test["Purchase"])
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue)) # p-değeri = 0.1083
# H0 hipotezi reddedilemez. Varyanslar homojen dagilmistir.

## AB Test

#Varsayımlar sağlanıyor, bağımsız iki örneklem t testi (parametrik test)
# H0: M1 = M2 (Iki grup ortalamaları arasında anlamli fark yoktur.)
# H1: M1 != M2 (Iki grup ortalamalari arasinda anlamli fark vardır)


from scipy import stats

test_istatistigi, pvalue = stats.ttest_ind(df_control["Purchase"],
                                            df_test["Purchase"],
                                           equal_var=True)

print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue)) #p-değeri = 0.3493

#  p >0.05 ->H0 reddedilmedi.Iki grup ortalamalari arasinda istatistiki olarak anlamli bir farklilik yoktur.

# Purchase degiskenine bakildiginda iki yöntem satis ortalamalari arasinda
# istatistiki olarak anlamli bir farklilik yoktur. Öneri olarak teste devam edilmesi
# önerilir.
# Öneri olarak dönüsüm oranina bakilmasi bir öneri.
# Neye göre fiyatlandirma yapilmis ve hangi degiskenler karsilastirilabilir.Bunun tartsimasi yapilabilir?
# Not: Sum veya mean alma arasindaki fark?

## AB Dönüsüm Orani
from statsmodels.stats.proportion import proportions_ztest
a,p=proportions_ztest(count=[df_test["Purchase"].mean(),df_control["Purchase"].mean()],
                         nobs=[df_test["Impression"].mean(),df_control["Impression"].mean()])
round(p,5)