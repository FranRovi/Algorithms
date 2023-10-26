-- Leet Code 1667. Fix Names in a Table

SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, LENGTH(name) -1))) AS name
FROM USERS
ORDER BY user_id ASC; 