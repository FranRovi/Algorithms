-- Leet Code 1757 SQL. Recyclabe and Low Fat Products

SELECT product_id
FROM Products
WHERE low_fats LIKE 'Y' AND recyclable LIKE 'Y';