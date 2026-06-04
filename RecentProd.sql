# Write your MySQL query statement below
WITH CTE AS (
    SELECT order_id, order_date,product_id,
    rank() OVER (PARTITION BY product_id ORDER BY order_date DESC) AS rnk
    FROM Orders

)
SELECT p.product_name, o.product_id, o.order_id, o.order_date FROM CTE o
LEFT JOIN
Products p
ON o.product_id = p.product_id
WHERE o.rnk = 1
ORDER BY product_name,product_id,order_id
