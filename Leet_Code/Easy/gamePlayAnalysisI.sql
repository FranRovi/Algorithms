-- Leet Code SQL Algo 511. Game Play Analysis I

SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id
ORDER BY player_id;