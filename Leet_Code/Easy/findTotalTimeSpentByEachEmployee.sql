-- Leet Code 1740. Find Total Time Spent by Each Employee

SELECT event_day AS 'day', emp_id, SUM(out_time - in_time) as 'total_time'
FROM Employees
GROUP BY event_day, emp_id;