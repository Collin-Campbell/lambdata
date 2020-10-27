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
=======
# accessing libraries through pipenv
import pandas as pd
import numpy as np



def df_missing_values(df):
    """counts missing values"""

    return df.isnull().sum()



def target_split(df, target_str):
    """splits target from df"""

    y = df[target_str]
    X = df.drop(columns=target_str)

    return y, X
>>>>>>> 4ef46b43cfe76cd92cc91152d7835e93e6befe06
