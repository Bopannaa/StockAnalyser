import numpy as np 
import pandas as pd

import os


class StockData:
    def __init__(self, path):
        self.path = path
        self.data_files = os.listdir(self.path)
        self.paths = [self.path + "/" + name for name in self.data_files]
        self.data = [pd.read_csv(path, index_col="Date") for path in self.paths]
        pass

    def get_data(self, column_name):
        data = [d[column_name] for d in self.data]
        return data

    def company_names(self):
        names = [name[:-4] for name in self.data_files]
        return names

    def get_filtered_binary_diff_output(self, column_name):
        data = [d.filter(items=[column_name]) for d in self.data]
        data = [d.diff().dropna() for d in data]
        data = [i.where(i > 0, 0) for i in data]
        data = [i.where(i == 0, 1) for i in data]
        return data 

    def get_filtered_diff_output(self, column_name):
        data = [d.filter(items=[column_name]) for d in self.data]
        data = [d.diff().dropna() for d in data]
        return data 
