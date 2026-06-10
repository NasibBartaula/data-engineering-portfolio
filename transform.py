import pandas as pd
import numpy as np
def transform_data(df):
    df["name"]=df["name"].str.title()
    df = df.replace(" ", np.nan)
    df=df.dropna()
    return df

    