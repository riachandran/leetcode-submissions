SELECT id, COUNT(*) as num FROM 
(
    SELECT requester_id as id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id FROM RequestAccepted
) as frd
GROUP BY id
ORDER BY num DESC, id ASC
LIMIT 1
