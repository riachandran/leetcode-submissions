# Write your MySQL query statement below
With MovieCTE AS (
    SELECT m.title, r.movie_id, r.user_id, r.rating, r.created_at FROM MovieRating r
    JOIN 
    Movies m
    ON r.movie_id = m.movie_id
),
UserCTE AS (
    SELECT c.title, c.movie_id, u.name, u.user_id, c.rating, c.created_at FROM MovieCTE c
    JOIN
    Users u
    ON c.user_id = u.user_id
),
highRates AS (
    SELECT name, COUNT(rating) as rnk FROM UserCTE 
    GROUP BY user_id
    ORDER BY rnk DESC, name ASC
    LIMIT 1
),
highAvg AS (
    SELECT title, AVG(rating) as avg_rate FROM UserCTE
    WHERE YEAR(created_at) = '2020' AND MONTH(created_at) = '02'
    GROUP BY movie_id
    ORDER BY avg_rate DESC, title ASC
    LIMIT 1
)
SELECT name as results FROM highRates
UNION ALL
SELECT title as results FROM highAvg
