# Write your MySQL query statement below
WITH HostWins AS (
    SELECT t.team_id, t.team_name,
    SUM(CASE WHEN m.host_goals > m.guest_goals THEN 3
        WHEN m.host_goals = m.guest_goals THEN 1 
        ELSE 0 END) AS num_points
FROM Teams t
LEFT JOIN
Matches m
ON t.team_id = m.host_team
GROUP BY t.team_id
),
GuestWins AS (
SELECT t.team_id, t.team_name,
    SUM(CASE WHEN m.guest_goals > m.host_goals THEN 3
        WHEN m.guest_goals = m.host_goals THEN 1 
        ELSE 0 END) AS num_points
FROM Teams t
LEFT JOIN
Matches m
ON t.team_id = m.guest_team
GROUP BY t.team_id
),
Wins AS (
SELECT * FROM HostWins
UNION ALL
SELECT * FROM GuestWins
)
SELECT team_id,team_name,SUM(num_points) as num_points
FROM Wins
GROUP BY team_id
ORDER BY num_points DESC, team_id ASC
