# Write your MySQL query statement below
SELECT name FROM SalesPerson s
LEFT JOIN 
Orders o
ON s.sales_id = o.sales_id
WHERE s.sales_id NOT IN (
    SELECT r.sales_id FROM Orders r 
    JOIN
    Company c
    ON r.com_id = c.com_id
    WHERE c.name = 'RED'
    GROUP BY r.sales_id
    )
GROUP BY name
