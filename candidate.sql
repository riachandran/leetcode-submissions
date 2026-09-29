# Write your MySQL query statement below
SELECT c.candidate_id FROM Candidates c
LEFT JOIN 
(SELECT interview_id, SUM(score) AS score FROM Rounds
GROUP BY interview_id) AS i
ON c.interview_id = i.interview_id
WHERE c.years_of_exp >= 2 AND i.score > 15
