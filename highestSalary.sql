# Write your MySQL query statement below
SELECT f.Department, f.Employee, f.Salary FROM (
    SELECT 
    e.name AS Employee, 
    e.salary AS Salary,
    e.departmentId,
    d.name AS Department,
    rank() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    LEFT JOIN
    Department d
    ON e.departmentId = d.id
) AS f
WHERE f.rnk = 1
