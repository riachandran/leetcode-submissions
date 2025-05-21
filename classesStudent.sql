# Write your MySQL query statement below
SELECT class FROM (
SELECT class,COUNT(student) as counts FROM Courses 
GROUP BY class
) as A
WHERE A.counts >= 5
