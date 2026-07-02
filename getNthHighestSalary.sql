CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      WITH CTE AS (
        SELECT salary,
        dense_rank() OVER (ORDER BY salary DESC) AS rnk
        FROM Employee
      )
        SELECT DISTINCT salary FROM CTE WHERE rnk = N
  );
END
