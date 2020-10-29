"""Lambdata - a collection of Data Science helper functions"""


<<<<<<< HEAD
# accessing libraries
import pandas as pd
import numpy as np

class DataFrame(pd.DataFrame):
    def __init__(self, filename):
        super().__init__(pd.read_csv(filename))
        self.filename = str(filename)

    def num_cells(self):
        """counts total number of cells in df"""
        return self.shape[0] * self.shape[1]

    def num_missing_values(self):
        """counts missing values"""
        return self.isnull().sum()

    def target__feature_split(self, target_col):
        """splits target from df"""
        self.y = self[str(target_col)]
        self.X = self.drop(columns=str(target_col))
