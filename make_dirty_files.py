import random
import pandas as pd


def make_duplicated_data(data, num_duplicates):
    random_indices = [random.randint(0, len(data) - 1) for _ in range(num_duplicates)]
    duplicates = data.iloc[random_indices]
    return pd.concat([data, duplicates], ignore_index=True)


num_duplicates1 = 200
num_duplicates2 = 5

data1 = pd.read_csv('source/business.retailsales.csv')
data2 = pd.read_csv('source/business.retailsales2.csv')

data1_1 = data1.iloc[:850]
data1_2 = data1.iloc[850:]

data2_1 = data2.iloc[:19]
data2_2 = data2.iloc[19:]

data1_1 = make_duplicated_data(data1_1, num_duplicates1)
data1_2 = make_duplicated_data(data1_2, num_duplicates1)

data2_1 = make_duplicated_data(data2_1, num_duplicates2)
data2_2 = make_duplicated_data(data2_2, num_duplicates2)

data1_1.to_csv('dirty_source/data1_1.csv', index=False)
data1_2.to_csv('dirty_source/data1_2.csv', index=False)
data2_1.to_csv('dirty_source/data2_1.csv', index=False)
data2_2.to_csv('dirty_source/data2_2.csv', index=False)
