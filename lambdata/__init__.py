"""Lambdata - a collection of Data Science helper functions"""


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