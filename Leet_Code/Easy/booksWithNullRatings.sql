-- Leet Code Algo 3358. Books with NULL ratings

SELECT book_id, title, author, published_year
FROM Books
WHERE rating IS NULL
ORDER BY book_id ASC;