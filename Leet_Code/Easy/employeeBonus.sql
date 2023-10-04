-- Leet Code 577. Employee Bonus

SELECT e.name, IFNULL(b.bonus, null) as 'bonus'
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;


