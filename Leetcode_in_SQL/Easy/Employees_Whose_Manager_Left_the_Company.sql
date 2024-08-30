# Write your MySQL query statement below
select employee_id  
from employees e
where (select count(employee_id) from employees where employee_id = e.manager_id) <= 0 and e.manager_id is not null and e.salary < 30000
order by employee_id