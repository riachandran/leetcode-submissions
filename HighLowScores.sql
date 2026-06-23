# Write your MySQL query statement below
WITH HighLowScores AS (
    SELECT exam_id, MIN(score) as lowest, MAX(score) as highest
    FROM Exam
    GROUP BY exam_id
),
QuietCount AS (
    SELECT e.student_id, SUM(IF((e.score = h.highest)|(e.score=h.lowest),1,0)) as cnt FROM Exam e
    LEFT JOIN
    HighLowScores h
    ON e.exam_id = h.exam_id
    GROUP BY e.student_id
)
SELECT q.student_id, s.student_name FROM QuietCount q
LEFT JOIN
Student s
ON q.student_id = s.student_id
WHERE q.cnt = 0
ORDER BY q.student_id
