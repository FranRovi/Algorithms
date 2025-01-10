-- Leet Code SQL Algo 1581. Customer Who Visited But Did Not Make Any Transactions

SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM Visits v 
LEFT JOIN Transactions t 
    ON t.visit_id = v.visit_id
WHERE t.transactions IS NULL
GROUP BY v.customer_id
ORDER BY v.customer_id;