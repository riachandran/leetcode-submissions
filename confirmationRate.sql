# Write your MySQL query statement below
SELECT sg.user_id, COALESCE(cf_ratio, 0) as confirmation_rate FROM Signups sg
LEFT JOIN
(SELECT user_id, round(sum(case when action='confirmed' then 1 else 0 end) / count(action),2) as cf_ratio FROM Confirmations
GROUP BY user_id) as cf
ON sg.user_id=cf.user_id
ORDER BY sg.time_stamp DESC. 
