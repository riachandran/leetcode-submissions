# Write your MySQL query statement below
WITH CTE AS (
    SELECT *,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rankN
    FROM Employee
)
SELECT MAX(salary) as SecondHighestSalary FROM CTE WHERE rankN = 2
