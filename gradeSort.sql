-- # Write your MySQL query statement below
SELECT student_id,course_id, grade FROM (
SELECT student_id,course_id, grade,row_number() over (PARTITION BY student_id ORDER BY grade DESC, student_id ASC, course_id ASC) as rnk FROM Enrollments
GROUP BY course_id,student_id
ORDER BY student_id ASC,  course_id ASC, grade DESC
)as Inloop
WHERE Inloop.rnk = 1
