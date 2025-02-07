-- Leet Code SQL Algo 1777. Products Price for Each Store

SELECT product_id,
    MAX(CASE WHEN store='store1' THEN price ELSE NULL END) AS store1,
    MAX(CASE WHEN store='store2' THEN price ELSE NULL END) AS store2,
    MAX(CASE WHEN store='store3' THEN price ELSE NULL END) AS store3
    FROM (
    SELECT product_id, store, price, row_number()OVER(PARTITION BY store) rn
        FROM Products
    ) tmp
GROUP BY product_id;