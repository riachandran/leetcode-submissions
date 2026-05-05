# Write your MySQL query statement below
WITH PerCount AS (
    SELECT p.id,p.name as person,c.name as name FROM Person p
    LEFT JOIN Country c ON p.phone_number LIKE CONCAT(c.country_code,'%')
),
Caller AS ( 
    SELECT c.caller_id, c.callee_id,pc.name as country, AVG(c.duration) as country_avg FROM Calls c
    LEFT JOIN PerCount pc 
    ON c.caller_id = pc.id OR c.callee_id = pc.id
    GROUP BY pc.name
)
SELECT country FROM Caller
WHERE country_avg > (SELECT AVG(c.duration) FROM Calls c LEFT JOIN PerCount pc ON c.caller_id = pc.id OR c.callee_id = pc.id)
