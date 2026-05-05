# Write your MySQL query statement below
SELECT DISTINCT seat_id
FROM (
    SELECT LAG(seat_id) OVER (ORDER BY seat_id) AS prev_seat,
    seat_id,
    LEAD(seat_id) OVER (ORDER BY seat_id) AS next_seat
    FROM Cinema
    WHERE free = 1
) t
WHERE prev_seat + 1 = seat_id OR next_seat - 1 = seat_id
ORDER BY seat_id
