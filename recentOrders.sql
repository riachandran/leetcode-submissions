# Write your MySQL query statement below
WITH CTE AS (
    SELECT order_id,
    order_date,
    customer_id,
    rank() OVER (PARTITION BY customer_id ORDER BY order_date DESC) as rnk
    FROM Orders
)
SELECT c.name as customer_name, o.customer_id, o.order_id, o.order_date FROM CTE o
LEFT JOIN
Customers c
ON o.customer_id = c.customer_id
WHERE o.rnk <= 3
ORDER BY customer_name ASC, customer_id ASC, order_date DESC
