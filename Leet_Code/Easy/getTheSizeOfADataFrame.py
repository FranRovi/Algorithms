# Leet Code Algo 2878. Get The Size of a DataFrame

import pandas as pd

def getDataframeSize(players):
    answer = []
    answer.append(len(players.index))
    answer.append(len(players.columns))
    return answer



