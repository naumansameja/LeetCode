# Write your MySQL query statement below
select e.name
from employee e
where (select count(managerId) from employee where managerId = e.id) >= 5
group by e.id
