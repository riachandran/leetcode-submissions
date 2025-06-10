# Write your MySQL query statement below
SELECT MAX(num) as num FROM (
SELECT num,COUNT(num) as countnum FROM MyNumbers
GROUP BY num
) as innerloop
WHERE innerloop.countnum = 1
