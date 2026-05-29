# Write your MySQL query statement below
WITH CTE AS (
    SELECT Wimbledon as player_id, COUNT(Wimbledon) AS cnt FROM Championships
    GROUP BY Wimbledon
    UNION ALL
    SELECT Fr_open as player_id, COUNT(Fr_open) AS cnt FROM Championships
    GROUP BY Fr_open
    UNION ALL
    SELECT US_open as player_id, COUNT(US_open) AS cnt FROM Championships
    GROUP BY US_open
    UNION ALL
    SELECT Au_open as player_id, COUNT(Au_open) AS cnt FROM Championships
    GROUP BY Au_open
)
SELECT c.player_id, p.player_name, SUM(c.cnt) as grand_slams_count FROM CTE c
LEFT JOIN
Players p
ON
c.player_id = p.player_id
GROUP BY c.player_id
