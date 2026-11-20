# Reflection 1: The boolean checks if the rows meets a certain conditions by determining if its true or false.
# Reflection 2: df['revenue] returns a single column of data as a series while df[['revenue']] returns a dataframe, which is a table containing one column.
# Reflection 3: I would choose panda over excel because it allows easier ways to automate data cleaning and analysis quicker when working on large datasets. 
# Excel forces you to manually filter and calculate information which does not help to get work done efficently. 


print("---Exercise 1---")


import pandas as pd 

df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("---Exercise 2---")

south = df[df['region'] == 'South']
print(len(south))
print(south.head())

print("---Exercise 3---")

top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

print("---Exercise 4---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())

print("---Exercise 5---")

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

print("---Exercise 6---")

print(df['region'].unique())
print(df['region'].value_counts())

print("---Exercise 7---")

selected = df[['region', 'product', 'revenue']]
print(selected.head())
print(selected.shape)

print("---Exercise 8---")

df.to_csv('data/explored.csv', index=False)
