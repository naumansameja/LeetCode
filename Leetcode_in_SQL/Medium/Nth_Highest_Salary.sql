CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
         
        select if(count(distinct salary) < N or N < 0, null, (select distinct salary from (select  distinct salary from Employee 
                order by salary desc
                limit N) as salaries

                order by salary asc
                limit 1))
                from Employee
                
  );
END