# Write your MySQL query statement below
WITH WindowDates AS (
    SELECT user_id, visit_date, LEAD(visit_date,1,'2021-1-1') OVER (PARTITION BY user_id ORDER BY visit_date) as win_date FROM UserVisits
)
SELECT user_id, MAX(DATEDIFF(win_date,visit_date)) as biggest_window FROM WindowDates
GROUP BY user_id
