-- Leet Code 1327. List the Products Ordered in a Period

SELECT Products.product_name, SUM(Orders.unit) as 'unit'
FROM Products
INNER JOIN Orders ON Orders.product_id = Products.product_id
WHERE Orders.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY Products.product_id
HAVING SUM(Orders.unit) >= 100;