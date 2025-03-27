-- # Leet Code SQL Algo 1350. Students With Invalid Departments

SELECT s.id, s.name
FROM Students s
LEFT JOIN Departments d
    ON s.department_id = d.id
WHERE s.department_id NOT IN
    (SELECT id FROM departments);