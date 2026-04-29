SELECT o.customer_id,c.name FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Product p ON o.product_id = p.product_id
WHERE YEAR(o.order_date) = 2020 AND MONTH(o.order_date) IN (6,7)
GROUP BY o.customer_id, c.name
HAVING 
    SUM(CASE WHEN MONTH(o.order_date)=6 THEN o.quantity*p.price ELSE 0 END) >= 100
    AND SUM(CASE WHEN MONTH(o.order_date)=7 THEN o.quantity*p.price ELSE 0 END) >= 100
