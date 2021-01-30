import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('diamonds')
df = df.select_dtypes(include=['float64', 'int64'])
df = df.dropna()
df.head()

df_table = df["table"]
df_table.head()

sns.boxplot(x = df_table);
plt.show()
