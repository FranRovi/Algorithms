-- Leet Code 175. Combine Two Tables

SELECT firstName, lastName, IFNULL (Address.city, null) as city, IFNULL (Address.state, null) as state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;