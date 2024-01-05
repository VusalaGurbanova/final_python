import pandas as pd

df=pd.DataFrame({'column':['a','b','c','a','b','c','a']})

unique_values=df['column'].unique()
one_hot_df=pd.DataFrame(0,index=df.index, columns=unique_values)



for value in unique_values:
    one_hot_df.loc[df['column']==value, value]=1

print(one_hot_df)
