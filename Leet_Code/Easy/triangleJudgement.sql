-- Leet Code 610. Triangle Judgement

SELECT *, IF(x + y > z AND y + z > x AND z + x > y, 'Yes', 'No') as 'triangle'
FROM Triangle;