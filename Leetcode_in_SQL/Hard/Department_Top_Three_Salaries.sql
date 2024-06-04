# Write your MySQL query statement below
select d.name Department, e.name Employee, e.salary Salary
from employee e join department d on e.departmentId = d.id
where e.salary >= (select salary from  (select distinct salary
                 from employee
                 where departmentId = e.departmentId
                  order by salary desc
                  limit 3) as three_highest_salaries
                  order by salary asc 
                  limit 1)
order by e.departmentId, e.salary desc
