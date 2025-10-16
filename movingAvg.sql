# Write your MySQL query statement below
WITH Daily AS (
    SELECT visited_on, SUM(amount) as amount FROM Customer
    GROUP BY visited_on
),
CTE AS (
    SELECT visited_on, SUM(amount) OVER (ORDER BY visited_on        RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) as amount, ROUND(AVG(amount)OVER (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW),2) as average_amount FROM Daily
ORDER BY visited_on
)
SELECT visited_on, amount, average_amount as average_amount FROM CTE
WHERE visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM daily), INTERVAL 6 DAY)
ORDER BY visited_on
