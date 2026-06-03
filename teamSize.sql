# Write your MySQL query statement below
SELECT e.employee_id, t.team_size FROM Employee e
LEFT JOIN (
    SELECT team_id, COUNT(team_id) AS team_size FROM Employee
    GROUP BY team_id
) AS t
ON e.team_id = t.team_id
