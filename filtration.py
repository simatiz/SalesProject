import pandas as pd


def concat_data(df1, df2):
    data = pd.concat([df1, df2], ignore_index=True)
    data = data.drop_duplicates()
    return data.reset_index(drop=True)


data1_1 = pd.read_csv('dirty_source/data1_1.csv')
data1_2 = pd.read_csv('dirty_source/data1_2.csv')
data2_1 = pd.read_csv('dirty_source/data2_1.csv')
data2_2 = pd.read_csv('dirty_source/data2_2.csv')

data1 = concat_data(data1_1, data1_2)
data2 = concat_data(data2_1, data2_2)



data1.to_csv('clear_source/data1.csv', index=False)
data2.to_csv('clear_source/data2.csv', index=False)
