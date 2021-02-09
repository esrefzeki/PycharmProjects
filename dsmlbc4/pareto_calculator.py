import pandas as pd

df_ = pd.read_excel("online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy()
# df10_11 = pd.read_hdf(r'D:\python\bootcamp\week_3\datasets\online_retail_II_y2010-2011.h5')
# df = df10_11.copy()
df.head()

##################################################
# Data Preparation
df = df[~df["Invoice"].str.contains("C", na=False)]
df = df[(df['Quantity'] > 0)]
df.dropna(inplace=True)
df["TotalPrice"] = df["Quantity"] * df["Price"]


# a groupby based pareto function
def pareto_value_calculator_for_groupby(dataframe, groupby_col, agg_col, agg_fuc, pareto_trh=80):
  dataframe = dataframe.groupby(groupby_col).agg({agg_col: agg_fuc}).sort_values(agg_col, ascending=False)
  dataframe.reset_index(inplace=True)
  dataframe['percents'] = dataframe[agg_col] * 100 / dataframe[agg_col].sum()
  dataframe['cumulative_percents'] = dataframe['percents'].cumsum()
  pareto_value = 100 - (dataframe.shape[0] - dataframe[dataframe['cumulative_percents'] >= pareto_trh].index[0]) * 100 / dataframe.shape[0]
  print(f'Pareto values at {pareto_trh}% after the groupby operation: ')
  return pareto_value


pareto_value_calculator_for_groupby(df, 'Customer ID', 'TotalPrice', 'sum')
# Output: 26.088960589997697

pareto_value_calculator_for_groupby(df, 'StockCode', 'TotalPrice', 'sum')
# Output: 21.173260572987715


# a general based pareto function
def pareto_value_calculator(dataframe, pareto_trh=80):
  num_cols_ = [col for col in dataframe.columns if ''.join([i for i in dataframe[col].dtypes.name if i.isalpha()]) in ['float', 'int'] ]
  pareto_values_ = {}
  for col_ in num_cols_:
    dataframe_a = dataframe.copy()
    dataframe = dataframe.sort_values(col_, ascending=False)
    dataframe.reset_index(inplace=True)
    dataframe['percents_'] = dataframe[col_] * 100 / dataframe[col_].sum()
    dataframe['cumulative_percents_'] = dataframe['percents_'].cumsum()
    pareto_value_ = 100 - (dataframe.shape[0] - dataframe[dataframe['cumulative_percents_'] >= pareto_trh].index[0]) * 100 / dataframe.shape[0]
    pareto_values_.update({col_: pareto_value_})
    dataframe = dataframe_a.copy()
  print(f'Pareto values at {pareto_trh}% for {len(num_cols_)} numeric columns: ')
  return pareto_values_


pareto_value_calculator(df[['Quantity', 'Price', 'TotalPrice', 'Country']])
pareto_value_calculator(df)

df_p = df.groupby('Customer ID').agg({'TotalPrice':'sum'}).sort_values('TotalPrice', ascending=False)
pareto_value_calculator(df_p)

