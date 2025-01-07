-- Leet Code SQL Algo 2985. Calculate Compressed Mean

SELECT ROUND((SUM(item_count * order_ocurrences)) / SUM(order_ocurrences), 2)
    AS average_items_per_order
FROM Orders;

