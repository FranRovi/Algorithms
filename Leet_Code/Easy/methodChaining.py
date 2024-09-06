# Leet Code Algo 2891. Method Chaining

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filterAnimals = animals.loc[animals['weight'] > 100]
    filterAnimalsDescending = filterAnimals.sort_values(by=['weight'], ascending=False)
    answer = pd.DataFrame(filterAnimalsDescending['name'])
    return answer