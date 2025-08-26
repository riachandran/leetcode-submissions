SELECT query_name, ROUND(AVG(rating/position),2) as quality, ROUND((SUM(case when rating < 3 then 1 else 0 end)*100)/COUNT(DISTINCT result),2) as poor_query_percentage 
FROM Queries
GROUP BY query_name
