# Leet Code Algo 2884 Pandas. Modify Column.


def modifyColumn(employees):
    updatedSalaries = employees.salary * 2
    employees['salary'] = updatedSalaries
    return employees