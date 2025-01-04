-- Leet Code SQL Algo 2082. The Number of Rich Customers

SELECT COUNT(*) AS rich_count FROM   
    (SELECT amount FROM STORE s
    WHERE amount > 500
    GROUP BY customer_id) s;
