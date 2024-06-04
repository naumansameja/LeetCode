# Write your MySQL query statement below
select d.name Department, e.name Employee, e.salary Salary
from Department d join Employee e on e.departmentId = d.id
where salary >= (select max(salary) from Employee where departmentId = d.id)