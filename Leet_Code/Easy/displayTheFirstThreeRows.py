# Leet Code 2879. Display the First Three Rows
import pandas as pd

def displayTheFirstThreeRows(employees):
    return employees.loc[0:2, :]
    