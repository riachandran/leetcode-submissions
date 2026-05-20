# Write your MySQL query statement below
SELECT employee_id FROM (
SELECT employee_id FROM Employees
UNION ALL
SELECT employee_id FROM Salaries
) A
GROUP BY employee_id
HAVING COUNT(employee_id) != 2
ORDER BY employee_id
