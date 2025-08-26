SELECT person_name FROM (
    SELECT person_name, weight, SUM(weight) OVER (ORDER by turn) as cumsum FROM Queue
 ) as i
 WHERE i.cumsum <= 1000
 ORDER BY cumsum DESC
 LIMIT 1
