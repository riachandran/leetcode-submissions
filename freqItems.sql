# Write your MySQL query statement below
WITH CTE AS (
    SELECT o.customer_id, o.product_id, p.product_name, RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(product_name) DESC) AS rnk FROM Orders o 
    LEFT JOIN Customers c ON o.customer_id = c.customer_id
    LEFT JOIN Products p ON o.product_id = p.product_id
    GROUP BY o.customer_id, p.product_name
)
SELECT customer_id, product_id, product_name FROM CTE 
WHERE rnk = 1
GROUP BY customer_id, product_id
