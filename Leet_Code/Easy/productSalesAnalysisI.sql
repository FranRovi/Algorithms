-- Leet Code 1068. Product Sales Analysis I

SELECT Product.product_name, Sales.year, Sales.price
FROM Product
INNER JOIN Sales ON Sales.product_id = Product.product_id;