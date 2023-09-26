-- Leet Code 1587. Bank Account Summary II

SELECT u.name as 'NAME', SUM(t.amount) as 'BALANCE'
FROM Users u
INNER JOIN Transactions t ON u.account = t.account
GROUP BY u.account
HAVING SUM(t.amount) > 10000;