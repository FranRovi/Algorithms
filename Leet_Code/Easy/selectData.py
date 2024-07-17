# Leet Code Algo 2880. Select Data

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    selectedStudent = students.loc[students.student_id == 101]
    studentData = {
        "name": selectedStudent.name,
        "age": selectedStudent.age
    }
    df = pd.DataFrame(studentData)
    return df