# Write your MySQL query statement below
SELECT o.customer_id, c.customer_name FROM Customers c
RIGHT JOIN
Orders o
ON c.customer_id = o.customer_id
GROUP BY o.customer_id
HAVING SUM(o.product_name = 'A') > 0 AND SUM(o.product_name = 'B') > 0 AND SUM(o.product_name = 'C') = 0
ORDER BY o.customer_id
