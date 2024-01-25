# Leet Code Algo 2888. Reshape Data: Concatenate

import pandas as pd

def reshapeData( df1, df2):
    return pd.concat([df1, df2], axis=0)