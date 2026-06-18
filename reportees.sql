# Write your MySQL query statement below
WITH DirectReportees AS (
    SELECT employee_id FROM Employees
    WHERE employee_id != 1 AND manager_id = 1
),
IndirectReportees AS (
    SELECT employee_id FROM Employees WHERE manager_id IN (SELECT employee_id FROM DirectReportees)
),
IndirectSecondReportees AS (
    SELECT employee_id FROM Employees WHERE manager_id IN (SELECT employee_id FROM IndirectReportees)
)
SELECT employee_id FROM DirectReportees
UNION ALL
SELECT employee_id FROM IndirectReportees
UNION ALL
SELECT employee_id FROM IndirectSecondReportees
