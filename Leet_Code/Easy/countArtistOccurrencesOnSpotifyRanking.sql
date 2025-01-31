-- Leet Code SQL Algo 2669. Count Artist Ocurrences On Spotify Ranking

SELECT artist, COUNT(*) as occurrences
FROM Spotify
GROUP BY artist
ORDER BY occurrences DESC, artist ASC;