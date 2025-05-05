SELECT name FROM Employee e JOIN 
(SELECT managerId, COUNT(managerId) FROM Employee
GROUP BY managerId
HAVING COUNT(managerId) >= 5) AS InLoop
WHERE e.id = InLoop.managerId
