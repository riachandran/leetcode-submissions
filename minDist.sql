# Write your MySQL query statement below
WITH CTE AS (SELECT 
    x,
    LAG(x,1) OVER (ORDER BY x) as dist
    FROM Point
)
SELECT MIN(x-dist) AS shortest FROM CTE WHERE dist IS NOT NULL
