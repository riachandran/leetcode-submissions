# Write your MySQL query statement below
SELECT s1.sale_date, (s1.sold_num - s2.sold_num) as diff FROM Sales s1
LEFT JOIN Sales s2
ON s1.sale_date = s2.sale_date AND s2.fruit = 'oranges'
WHERE s1.fruit = 'apples'
