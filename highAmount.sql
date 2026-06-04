# Write your MySQL query statement below
SELECT t.transaction_id FROM (
    SELECT 
        transaction_id,
        rank() OVER (PARTITION BY DATE(day) ORDER BY amount DESC) AS rnk
        FROM Transactions
) AS t
WHERE t.rnk = 1
ORDER BY t.transaction_id 
