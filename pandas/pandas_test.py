import pandas as pd

df2 = pd.read_csv("world_population.csv",index_col="Capital") 
print(df2)
df2.set_index("Country",inplace=True)
print(df2.loc["Andorra"])
print(df2.iloc[1])
df2.reset_index(inplace=True)
df2.set_index(["Continent","Country"],inplace=True)
df2.sort_index(ascending=False,inplace=True)
print(df2)