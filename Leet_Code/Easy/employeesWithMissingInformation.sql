-- Leet Code 1965. Employees With Missing Information

SELECT employee_id   
FROM (
    SELECT Employees.employee_id, IFNULL(Employees.name, null) AS name, IFNULL(Salaries.salary, null) AS salary
    FROM Employees
    LEFT JOIN Salaries ON Employees.employee_id = Salaries.employee_id
    UNION
    SELECT Salaries.employee_id, IFNULL(Employees.name, null) AS name, IFNULL(Salaries.salary, null) AS salary
    FROM Employees
    RIGHT JOIN Salaries ON Employees.employee_id = Salaries.employee_id
) AS sub
WHERE sub.name IS NULL OR sub.salary IS NULL
ORDER BY employee_id ASC;