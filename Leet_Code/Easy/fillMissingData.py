# Leet Code Algo 2887. Fill Missing Data

def fillMissingData(products):
    products['quantity'].fillna(0, inplace= True)
    return products 