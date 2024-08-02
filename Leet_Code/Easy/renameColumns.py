# Leet Code Algo 2885. Rename Columns (Pandas)

import pandas as pd

def renameColumns(students):
    students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'}, inplace=True)
    return students