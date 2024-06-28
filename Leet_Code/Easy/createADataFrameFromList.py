# Leet Code Algo 2877. Create a DataFrame from List

import pandas as pd

def createDataframe(student_data):
    df = pd.DataFrame(student_data, columns=['students_id', 'age'])
    return df