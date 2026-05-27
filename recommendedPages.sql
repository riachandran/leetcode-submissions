# Write your MySQL query statement below
WITH CTE AS (
    SELECT user2_id as user_id FROM Friendship WHERE user1_id = 1
    UNION 
    SELECT user1_id as user_id FROM Friendship WHERE user2_id = 1
)
SELECT DISTINCT page_id as recommended_page FROM Likes 
WHERE user_id IN (SELECT DISTINCT user_id FROM CTE) AND page_id NOT IN (
    SELECT page_id FROM Likes WHERE user_id = 1
)
