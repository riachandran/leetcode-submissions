SELECT A.id, COUNT(*) as num FROM (
    SELECT requester_id as id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id FROM RequestAccepted
) AS A
GROUP BY A.id
ORDER BY num DESC, A.id ASC
LIMIT 1
