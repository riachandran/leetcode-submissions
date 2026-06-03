# Write your MySQL query statement below
SELECT p.player_id, p.device_id FROM 
(
    SELECT player_id,
        device_id,
        rank() OVER (PARTITION BY player_id ORDER BY event_date) AS rnk
    FROM Activity
) AS p
WHERE p.rnk = 1
