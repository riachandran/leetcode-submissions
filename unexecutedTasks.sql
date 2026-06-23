# Write your MySQL query statement below
WITH RECURSIVE r AS(
    SELECT task_id, subtasks_count AS subtask_id FROM Tasks
    UNION ALL
    SELECT task_id, subtask_id - 1 FROM r WHERE subtask_id > 1
)
SELECT * FROM r
EXCEPT
SELECT * FROM Executed
