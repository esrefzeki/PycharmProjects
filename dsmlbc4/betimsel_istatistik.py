#BETİMSEL İSTATİSTİK

import seaborn as sns
import researchpy as rp

tips = sns.load_dataset("tips")
df = tips.copy()
df.head()
df.describe().T

rp.summary_cont(df[["total_bill", "tip", "size"]]) #Sayısal değişken bazında inceleme için _cont

rp.summary_cat(df[["sex", "smoker", "day"]]) #Kategorik değişken bazında inceleme için _cat

df[["tip", "total_bill"]].cov() #Kovaryans inceleme için

df[["tip", "total_bill"]].corr() #Korelasyona bakmak için
