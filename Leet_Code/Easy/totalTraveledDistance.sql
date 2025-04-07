-- Leet Code Algo SQL 2837. Total Traveled Distance

SELECT u.user_id, u.name, IFNULL(SUM(distance),0) AS 'traveled distance'
FROM Users u
LEFT JOIN Rides r ON u.user_id = r.user_id
GROUP BY u.user_id
ORDER BY u.user_id 