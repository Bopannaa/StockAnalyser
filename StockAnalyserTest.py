import random
import numpy as np
import pandas as pd
from StockData import StockData
import RandomSequence

stock_data = StockData(path="data")

dfs = stock_data.get_filtered_binary_diff_output(column_name="Close")
# dfs = [df['Close'].apply(int) for df in dfs]
df_sizes = [len(df) for df in dfs]
df_sizes = np.array(df_sizes)

percentages = []


def printmanytimes():
    np.random.SeedSequence()
    # df_rand = np.array(np.random.randint(2, size=df_sizes.max()))
    # df_rand = RandomSequence.get_random_binary(df_sizes.max())
    df_rand = RandomSequence.get_random_binary(df_sizes.max())

    df = dfs[0]

    df["Rand"] = df_rand[: len(df)]
    df["Close"] = df["Close"].apply(int)
    df["Result"] = df["Close"] & df["Rand"]
    res_sum = df["Result"].sum()
    rand_sum = df["Rand"].sum()
    percentage = (100 * res_sum) / rand_sum
    percentages.append(percentage)
    print("df_length: ", len(df), "rand_sum: ", rand_sum)


for i in range(100):
    printmanytimes()

# percentages = np.array(percentages)
# print(percentages.max())
