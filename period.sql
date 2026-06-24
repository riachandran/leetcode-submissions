# Write your MySQL query statement below
WITH CTE AS (
    SELECT fail_date AS date,
    'failed' AS period_state FROM Failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION ALL
    SELECT success_date as date,
    'succeeded' AS period_state FROM Succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
    ORDER BY date
),
RankCTE AS (
    SELECT date,
    period_state,
    ROW_NUMBER() OVER (ORDER BY date) - RANK() OVER (PARTITION BY period_state ORDER BY date) AS rnk
    FROM CTE
    ORDER BY date
)
SELECT period_state,MIN(date) AS start_date, MAX(date) AS end_date FROM RankCTE
GROUP BY rnk,period_state
ORDER BY start_date
