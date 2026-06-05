# Write your MySQL query statement below
WITH empProject AS (
    SELECT e.employee_id, e.experience_years,p.project_id FROM Employee e
    RIGHT JOIN
    Project p
    ON e.employee_id = p.employee_id
),
rankExp AS (
    SELECT *,
            dense_rank() OVER (PARTITION BY project_id ORDER BY experience_years DESC) as rnk
    FROM empProject
)
SELECT project_id,employee_id FROM rankExp WHERE rnk = 1
