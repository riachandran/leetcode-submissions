# Write your MySQL query statement below
SELECT s.seller_name FROM Orders o 
RIGHT JOIN
Seller s
ON o.seller_id = s.seller_id
WHERE s.seller_id NOT IN (SELECT seller_id FROM Orders WHERE YEAR(sale_date) = 2020 GROUP BY seller_id)
ORDER BY s.seller_name
