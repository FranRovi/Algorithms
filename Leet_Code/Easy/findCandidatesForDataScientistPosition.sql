-- Leet Code Algo 3051. Find Candidate for Data Scientist Position

SELECT candidate_id
FROM Candidates
WHERE skill IN ("Python", "Tableau", "PostgreSQL")
GROUP BY candidate_id
HAVING COUNT(skill) = 3
ORDER BY candidate_id ASC; 