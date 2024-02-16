# Leet Code Algo 2881. Create a New Column

def createANewColumn(employees):
    employees['bonus'] = employees['salary'] * 2
    return employees
