# Write your MySQL query statement below
SELECT c.customer_id FROM Customer c
JOIN Product p
ON c.product_key = p.product_key
GROUP BY c.customer_id
HAVING count(distinct c.product_key) = (select count(product_key) FROM Product)
