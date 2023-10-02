-- Leet Code 1378. Replace Employee ID With The Unique Identifier

SELECT IFNULL (unique_id, null) as 'unique_id', Employees.name
FROM EmployeeUNI
RIGHT JOIN Employees ON Employees.id = EmployeeUNI.id;