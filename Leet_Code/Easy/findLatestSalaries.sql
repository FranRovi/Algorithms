-- Leet Code SQL Algo 2668. Find Latest Salaries

SELECT emp_id, firstname, lastname, MAX(salary) as salary, department_id
FROM salary
GROUP BY emp_id
ORDER BY emp_id;