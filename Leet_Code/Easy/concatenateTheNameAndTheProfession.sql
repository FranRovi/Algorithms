-- Leet Code SQL Algo 2504. Concatenate the Name and the Profession

SELECT person_id, 
    CONCAT(name, "(",SUBSTRING(profession, 1, 1),")") AS name
FROM Person
ORDER BY person_id DESC;